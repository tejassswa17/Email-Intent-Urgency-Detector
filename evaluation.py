from dotenv import load_dotenv
load_dotenv()

from model import chain
from langfuse.langchain import CallbackHandler
from langfuse import observe

langfuse_handler = CallbackHandler()

test_cases = [
    "Please fix this issue immediately.",
    "The server is down and customers cannot access the platform.",
    "Can you provide an update on my request?",
    "Thank you for your assistance with this matter.",
    "We have completed the scheduled maintenance.",
    "Please approve the attached invoice today.",
    "The payment system is not working properly.",
    "What are your customer support hours?",
    "Kindly share the latest project report.",
    "This issue remains unresolved after several follow-ups.",
    "Our presentation starts in an hour and the application is unavailable.",
    "Please grant access to the dashboard.",
    "The latest update improved system performance.",
    "Several users are unable to log in.",
    "Could you explain the pricing plan details?",
    "Immediate action is required to resolve this outage.",
    "We detected suspicious activity on your account.",
    "Please schedule a meeting for next week.",
    "The report has been successfully submitted.",
    "I am disappointed with the quality of service received.",
    "Can you help me reset my password?",
    "No action is required from your side.",
    "The website is loading very slowly today.",
    "Looking forward to your response.",
    "asdf qwerty random text with no clear meaning.",

    "My order has not arrived yet.",
    "Could you send the updated contract?",
    "The application keeps crashing after login.",
    "Thank you for the quick turnaround.",
    "When will my refund be processed?",
    "Please escalate this matter immediately.",
    "The dashboard metrics appear incorrect.",
    "Can I change my subscription plan?",
    "We have successfully completed testing.",
    "The checkout page is not loading.",
    "Please review the attached document.",
    "I need access to the production environment.",
    "Our customers are reporting frequent timeouts.",
    "Could you share the API documentation?",
    "The issue has been resolved. Thank you.",
    "Why was my account suspended?",
    "Please update my contact information.",
    "The service outage is affecting our business.",
    "Can you confirm receipt of my application?",
    "Your team did a great job on this release.",
    "The billing amount seems incorrect.",
    "We are planning maintenance this weekend.",
    "Please prioritize this ticket.",
    "I am unable to upload files.",
    "Can you explain the recent charges?",

    "The mobile app is not responding.",
    "Thank you for resolving the bug.",
    "What is the expected delivery date?",
    "Please unlock my account.",
    "The new feature works perfectly.",
    "Our payment gateway is unavailable.",
    "Could you provide a status update?",
    "The data export is incomplete.",
    "We have updated our company address.",
    "Please send the meeting agenda.",
    "The system is performing much better now.",
    "I cannot access my purchase history.",
    "Can you help me configure the integration?",
    "Several users are reporting login failures.",
    "The issue is becoming critical for our team.",
    "When is the next software release scheduled?",
    "Please process this request urgently.",
    "The report generation feature is broken.",
    "We appreciate your excellent support.",
    "My invoice contains duplicate charges.",
    "Can I get an update on ticket #1234?",
    "The website appears to be offline.",
    "Please share the onboarding guide.",
    "The migration was completed successfully.",
    "random words abc xyz nothing meaningful here"
]

@observe(name="Email Intent & Urgency Detection Application Evaluation")
def run_evaluation():

    for idx, email in enumerate(test_cases, start=1):

        prediction = chain.invoke(
            {"problem": email},
            config={"callbacks": [langfuse_handler]}
        )

        print("\n" + "=" * 70)
        print(f"TEST CASE {idx}")

        print("\nINPUT EMAIL:")
        print(email)

        print("\nOUTPUT:")
        print(prediction.model_dump())

run_evaluation()