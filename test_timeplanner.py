import pytest
from timeplanner import calculate_bmi, suggest_plan

# -------------------------
# Test: BMI Calculation
# -------------------------
def test_bmi_normal_case():
    assert round(calculate_bmi(70, 175), 2) == 22.86

def test_bmi_zero_height():
    with pytest.raises(ZeroDivisionError):
        calculate_bmi(70, 0)

def test_bmi_edge_case():
    assert round(calculate_bmi(50, 150), 2) == 22.22

# -------------------------
# Test: Workout Plan Recommendation
# -------------------------
def test_suggest_underweight_plan():
    bmi = 17.0
    result = suggest_plan(bmi)
    assert "20 mins light exercise" in result
    assert "High-calorie" in result

def test_suggest_healthy_plan():
    bmi = 22.0
    result = suggest_plan(bmi)
    assert "30 mins moderate exercise" in result
    assert "Balanced diet" in result

def test_suggest_overweight_plan():
    bmi = 27.0
    result = suggest_plan(bmi)
    assert "45 mins cardio" in result or "45 mins" in result
    assert "Low-carb" in result

def test_suggest_obese_plan():
    bmi = 35.0
    result = suggest_plan(bmi)
    assert "60 mins intense cardio" in result
    assert "Very low-carb" in result
