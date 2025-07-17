from test_samples import test_samples
from docstring_generator import generate_docstring  # Your function
import re

def manual_score(generated, expected):
    if generated.lower().strip() == expected.lower().strip():
        return 5
    elif expected.lower() in generated.lower():
        return 4
    elif len(set(generated.split()) & set(expected.split())) > 3:
        return 3
    else:
        return 2

results = []
correct = 0

for sample in test_samples:
    generated = generate_docstring(sample["code"])
    # Clean up the output for fair comparison
    generated = re.sub(r'["\'`]', "", generated.strip())

    expected = sample["expected"]
    score = manual_score(generated, expected)

    if score >= 4:
        correct += 1

    results.append({
        "code": sample["code"],
        "expected": expected,
        "generated": generated,
        "score": score
    })

accuracy = correct / len(results) * 100

# Final report
print(f"\n✅ Accuracy: {accuracy:.2f}% on {len(results)} test cases\n")

# Print individual results
for i, res in enumerate(results, 1):
    print(f"--- Test {i} ---")
    print("Code:")
    print(res["code"])
    print("Generated Docstring:")
    print(res["generated"])
    print("Expected Docstring:")
    print(res["expected"])
    print(f"Score: {res['score']}/5\n")
