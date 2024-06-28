meta_distiller_prompt = """
As an expert in analyzing and generalizing problem-solving approaches, your task is to distill information from call center records about equipment maintenance and parts prediction. Your goal is to extract key details and create a generalizable template for processing such records.
When presented with a call center record, please analyze it thoroughly and extract the following information:

When presented with a call center record, please analyze it and respond with the following:

1. Core task summarization:
    a. Identify the basic type of problem (e.g., data extraction, equipment diagnosis)
    b. Describe the core challenges (e.g., interpreting technical jargon, linking issues to solutions)
    c. Analyze the most efficient way to process these records
2. Solution Steps Description:
    Outline the general steps for processing these records, including:
        a. How to define the problem
        b. Determine key variables
        c. List important constraints or patterns
        d. Choose appropriate extraction and analysis strategies
        e. Verify the accuracy of extracted information
3. General Answer Template:
    Propose a template that can be widely applied to this type of record, including:
        a. Key variables to extract
        b. Potential functions or methods for information extraction
        c. A base class or interface definition for record processing

Your response should be structured as follows:
1. Core Task Summary:
   [Your analysis here]

2. Solution Steps:
   [Step-by-step outline here]

3. General Answer Template:
   [Proposed template or class definition here]

4. Example Implementation:
   [Brief example of how the template could be used]

Important guidelines:
    a. Ensure your response is highly concise and structured
    b. Focus on creating a generalizable method, not just solving a specific instance
    c. Consider how your template could handle variations in record format or content
    d. Prioritize flexibility and robustness in your proposed approach

Your task is to distill the problem-solving approach, not to provide specific solutions. Aim for a template that can be easily adapted to various equipment maintenance scenarios.

Here is the record:
{{data}}
"""

