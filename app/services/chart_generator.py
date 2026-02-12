import plotly.graph_objects as go

def generate_bar_chart(skill_data):

    skills = list(skill_data.keys())
    counts = list(skill_data.values())

    fig = go.Figure(
        data=[
            go.Bar(
                x=skills,
                y=counts,
                marker_color="#2563eb"
            )
        ]
    )

    fig.update_layout(
        title="Top 10 In-Demand Skills",
        xaxis_title="Skills",
        yaxis_title="Count",
        template="plotly_white"
    )

    return fig.to_html(full_html=False)


def generate_pie_chart(data):

    labels = list(data.keys())
    values = list(data.values())

    fig = go.Figure(
        data=[go.Pie(labels=labels, values=values)]
    )

    fig.update_layout(
        title="Work Type Distribution",
        template="plotly_white"
    )

    return fig.to_html(full_html=False)
