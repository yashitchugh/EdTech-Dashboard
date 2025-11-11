from langsmith import traceable
import time


@traceable(run_type="llm", name="Gemini Audio Analysis")
def call_gemini_api():
    print("Calling Gemini...")
    time.sleep(3) # Simulate a 3-second API call
    print("Gemini call complete.")
    return {"feedback": "Your answer was very clear."}