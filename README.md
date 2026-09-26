# Factory AI Agent

A learning project for understanding how AI agents work and how to combine an LLM with deterministic Python business logic.

## Project Goal

Build an AI agent for a small factory that can understand production requests, use tools, access factory data, and calculate purchasing requirements.

## Architecture

User
  ↓
LLM (Qwen)
  ↓
Tool Selection
  ↓
Python Tools
  ↓
Business Data / Calculations
  ↓
Tool Result
  ↓
LLM
  ↓
Final Answer

## Current Tools

### inventory_tool

Returns the current factory inventory.

### product_requirements_tool

Returns the materials required to manufacture a product.

### purchase_list_tool

Calculates the exact materials that need to be purchased for a production order.

## Example

User request:

"I need to manufacture 2 kitchen cabinets. What materials should I purchase?"

The LLM selects:

purchase_list_tool(
    product_name="kitchen_cabinet",
    quantity=2
)

Python calculates:

- MDF Board: 2
- Handles: 3

## What I Learned

- Difference between an LLM and an AI Agent
- Tool calling
- Tool arguments
- Tool results
- Agent loops
- Using multiple tools
- Separating AI reasoning from business logic
- Deterministic calculations with Python
- LLMs should not be the source of truth for critical calculations

## Main Design Principle

The LLM understands the user's intent and decides which action to take.

Python tools handle deterministic calculations, business rules, and reliable data access.

## Technology

- Python
- Ollama
- Qwen3 1.7B
- JSON
- Git
