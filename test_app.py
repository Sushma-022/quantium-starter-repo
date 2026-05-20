from app import app
def test_visualizer_element(dash_duo):

    dash_duo.start_server(app)

    dash_duo.wait_for_page()

    header= dash_duo.find_element("h1")
    assert header.text == "Soul Foods: Pink Morsel Sales Visualizer"

    region_picker = dash_duo.find_element("#region_picker")
    assert region_picker is not None
    
    graph = dash_duo.find_element("#sales_line_chart")
    assert graph is not None