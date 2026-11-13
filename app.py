from langgraph.graph import END, START, StateGraph
import streamlit as st
from typing import TypedDict


# Define state
class BMIState(TypedDict):
  weight_kg: float
  height_m: float
  bmi: float
  category: str


# Define nodes
def calculate_bmi(state: BMIState) -> BMIState:
  weight = state["weight_kg"]
  height = state["height_m"]
  bmi = weight / (height**2)
  state["bmi"] = round(bmi, 2)
  return state


def label_bmi(state: BMIState) -> BMIState:
  bmi = state["bmi"]
  if bmi < 18.5:
    state["category"] = "underweight"
  elif 18.5 <= bmi < 25:
    state["category"] = "normal"
  elif 25 <= bmi < 30:
    state["category"] = "overweight"
  else:
    state["category"] = "obese"
  return state


# Build and cache workflow
@st.cache_resource
def get_workflow():
  graph = StateGraph(BMIState)
  graph.add_node("calculate_bmi", calculate_bmi)
  graph.add_node("label_bmi", label_bmi)
  graph.add_edge(START, "calculate_bmi")
  graph.add_edge("calculate_bmi", "label_bmi")
  graph.add_edge("label_bmi", END)
  return graph.compile()


workflow = get_workflow()

st.title("⚖️ BMI Calculator")
st.write("Enter your weight and height below to run your LangGraph workflow.")

weight_input = st.number_input(
    "Weight (kg)", min_value=10.0, max_value=300.0, value=80.0
)
height_input = st.number_input(
    "Height (meters)", min_value=0.5, max_value=2.5, value=1.73
)

if st.button("Run Workflow"):
  initial_state = {"weight_kg": weight_input, "height_m": height_input}
  final_state = workflow.invoke(initial_state)

  st.success(f"Calculated BMI: *{final_state['bmi']}*")
  st.info(f"Category: *{final_state['category'].capitalize()}*")