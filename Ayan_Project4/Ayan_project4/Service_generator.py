# service_generator.py
from google.cloud import aiplatform
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

class ServiceGenerator:
    def __init__(self):
        # Set your Google Cloud project ID and location
        self.project_id = "your-google-cloud-project-id"
        self.location = "your-location"  # e.g., "us-central1"
        
        # Initialize the AI Platform
        aiplatform.init(project=self.project_id, location=self.location)

        self.prompt_template = PromptTemplate(
            input_variables=["request"],
            template="""You are an AI assistant that generates backend service code based on developer requirements. 
            Generate a service code for the following request: {request}"""
        )
        self.service_chain = LLMChain(llm=self.get_gemini_llm(), prompt=self.prompt_template)

    def get_gemini_llm(self):
        # Replace with your Gemini model endpoint or configuration
        # This assumes a hypothetical `Gemini` class, adjust accordingly based on actual library
        # Note: This might need further implementation based on the actual Gemini API.
        return aiplatform.gapic.PredictionServiceClient().predict(
            endpoint="your-endpoint",  # specify your endpoint here
            instances=[])
        
    def generate_service_code(self, request_text):
        response = self.service_chain.run(request=request_text)
        return response

    def generate_service_code_with_complex_logic(self, request_text, business_logic=None):
        response = self.service_chain.run(request=request_text)
        if business_logic:
            response += f"\n# Business Logic: {business_logic}"
        return response
