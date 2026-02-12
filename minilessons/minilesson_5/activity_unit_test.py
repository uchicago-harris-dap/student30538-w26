"""
Activity: Unit Testing Functions and Data Quality
===================================================

In this activity, you will:
1. Test a function with different inputs
2. Test data quality after merging DataFrames

Instructions:
- Complete the TODO sections below
- Run this file: python activity_unit_test.py
- If all tests pass, you'll see "All tests passed!"
- If any test fails, you'll see an AssertionError
"""

import pandas as pd

# ============================================================================
# PART 1: Testing Functions
# ============================================================================


def is_passing_grade(grade):
    """Check if a grade is passing (70 or above)"""
    return grade >= 70


# TODO: Write a test for passing grade (>= 70)
def test_passing_grade():
    # Your assertion here
    assert is_passing_grade(85) == True, "Expected grade 85 to be passing"
    print("Test passed: Grade 85 is passing")


# TODO: Write a test for failing grade (< 70)
def test_failing_grade():
    # Your assertion here
    assert is_passing_grade(65) == False, "Expected grade 65 to be failing"
    print("Test passed: Grade 65 is failing")


# TODO: Write a test for the edge case (exactly 70)
def test_edge_case_70():
    # Your assertion here
    assert is_passing_grade(70) == True, "Expected grade 70 to be passing"
    print("Test passed: Grade 70 is passing (edge case)")


# ============================================================================
# PART 2: Testing Data Quality
# ============================================================================

def create_student_data():
    """Create and merge student grades with names"""

    # DataFrame with student IDs and grades
    grades = pd.DataFrame({
        'id': [1, 2, 3],
        'grade': [85, 92, 88]
    })

    # DataFrame with student IDs and names
    names = pd.DataFrame({
        'id': [2, 3, 4],
        'name': ['Alex', 'Yuri', 'Ralph']
    })

    # Merge the two DataFrames
    students = grades.merge(names, on='id', how='left')
    return students


# TODO: Test that we have the correct number of rows
def test_row_count():
    students = create_student_data()

    # Your assertion here
    assert len(students) == 3, f"Expected 3 rows, got {len(students)}"

    print("Test passed: Correct row count (3 rows)")


# TODO: Test that all required columns are present
def test_columns_exist():
    # Your assertion here
    students = create_student_data()
    expected_columns = ['id', 'grade', 'name']

    # Your assertion here
    for column in expected_columns:
        assert column in students.columns, f"Expected column '{column}' to be present"

    print("Test passed: All required columns present")


# TODO: Test that we don't have unexpected missing values in critical columns
def test_no_missing_grades():
    students = create_student_data()

    # The .isnull() method returns True for missing values
    # Your assertion here
    assert students['grade'].isnull().sum() == 0, "Expected no missing grades"

    print("Test passed: No missing grades")


# ============================================================================
# Do not change: RUN ALL TESTS
# ============================================================================

if __name__ == "__main__":

    print("PART 1: Testing Functions")
    print("-" * 60)

    test_passing_grade()
    test_failing_grade()
    test_edge_case_70()

    print("PART 2: Testing Data Quality")
    print("-" * 60)

    test_row_count()
    test_columns_exist()
    test_no_missing_grades()

    print("-" * 60)
    print("All tests pass")
    print("-" * 60)
