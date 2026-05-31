import anthropic
import os
from dotenv import load_dotenv

# Load environment variables (for API key)
load_dotenv()

class GenAIEngine:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.auth_error = None

        if not self.api_key:
            self.client = None
            self.auth_error = "Anthropic API key not found. Please set ANTHROPIC_API_KEY in .env."
            print(f"Warning: {self.auth_error}")
        else:
            try:
                self.client = anthropic.Anthropic(api_key=self.api_key)
            except Exception as exc:
                self.client = None
                self.auth_error = f"Failed to initialize Anthropic client: {exc}"
                print(f"Warning: {self.auth_error}")

    def _api_unavailable_message(self):
        if self.auth_error:
            return f"GenAI is unavailable: {self.auth_error}"
        return "GenAI is unavailable without a valid Anthropic API key."

    def _call_model(self, prompt, system, **kwargs):
        if not self.client:
            return self._api_unavailable_message()

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                system=system,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return message.content[0].text
        except anthropic.AuthenticationError:
            return "GenAI is unavailable because the Anthropic API key is invalid. Please update `.env` with a valid key."
        except Exception as exc:
            return f"GenAI is unavailable due to an API error: {exc}"

    def get_demand_insights(self, data_summary):
        """
        Generates narrative insights based on a summary of the forecast.
        """
        prompt = f"""
        You are a Retail Demand Analyst. Based on the following forecast data summary,
        provide 3-4 key strategic insights and recommendations for the store manager.
        Summarize trends, potential risks, and optimization tips (e.g., inventory or staffing).

        Data Summary:
        {data_summary}

        Keep it professional, concise, and actionable.
        """

        return self._call_model(
            prompt,
            system="You are an expert retail consultant.",
            max_tokens=1000,
            temperature=0.7,
        )

    def chat_with_analyst(self, user_query, data_context):
        """
        Conversational interface to ask questions about the demand forecast.
        """
        prompt = f"""
        User Question: {user_query}

        Context regarding the forecast:
        {data_context}

        Answer the user's question using the provided context. If the answer isn't in the context,
        provide a logical reasoning based on retail best practices.
        """

        return self._call_model(
            prompt,
            system="You are a helpful retail demand assistant.",
            max_tokens=1000,
            temperature=0.5,
        )

    def explain_anomaly(self, anomaly_summary):
        """
        Claude explains why a specific data point might be an anomaly.
        """
        prompt = f"""
        Analyze this retail sales anomaly and provide 2-3 possible real-world reasons why this happened.
        Consider factors like logistics, local events, data errors, or extreme weather.

        Anomaly Details:
        {anomaly_summary}
        """

        return self._call_model(
            prompt,
            system="You are a data forensics expert in retail.",
            max_tokens=800,
            temperature=0.6,
        )

if __name__ == "__main__":
    # Test (requires API key in .env)
    engine = GenAIEngine()
    test_summary = "Predicted Sales: $15,000, Promo: Yes, Competition: Close, Month: December."
    # print(engine.get_demand_insights(test_summary))
