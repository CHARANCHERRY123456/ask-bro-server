def get_info_from_data(input: dict) -> dict:
    # For now, dummy
    return {"sql": "SELECT * FROM r20e3s1 LIMIT 10", "data": [], "content": "Here's a preview"}

def generate_plotly_chart(input: dict) -> dict:
    # Dummy chart
    return {
        "type": "bar",
        "title": "Sample Chart",
        "labels": ["A", "B", "C"],
        "datasets": [{"label": "Marks", "data": [10, 20, 30]}],
        "description": "This is a test chart."
    }
