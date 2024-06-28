meta_distiller_prompt = """
As an expert in analyzing call center records for equipment maintenance, your task is to identify patterns and create a framework for extracting key information from dispatcher-technician conversations. Your goal is to develop a systematic approach that can be applied manually to analyze these records efficiently.
When presented with a call center record, please provide the following:

1. Core Information Categories: Identify the main categories of information typically present in these records (e.g., equipment details, reported issues, technician actions).
2. Key Patterns and Indicators: Describe patterns or indicators that help identify important information within each category (e.g., specific phrases, formatting, or sequence of information).
3. Information Extraction Framework: Develop a step-by-step framework for manually extracting and organizing the relevant information from these records.
4. Challenges and Considerations: Highlight potential challenges in the extraction process and considerations for maintaining accuracy and consistency.
5. Standardization Suggestions: Propose ideas for standardizing the extracted information to ensure consistency across different records.

1. Core Information Categories:
   [List and briefly describe main categories]

2. Key Patterns and Indicators:
   [Describe patterns for each category]

3. Information Extraction Framework:
   [Step-by-step process for manual extraction]

4. Challenges and Considerations:
   [List potential difficulties and important factors]

5. Standardization Suggestions:
   [Ideas for maintaining consistency in extracted data]

6. Example Application:
   [Brief demonstration of how to apply this framework to a sample record]

Guidelines:

a. Focus on creating a flexible, manual approach that doesn't require coding
b. Emphasize pattern recognition and critical thinking skills
c. Consider how this framework could be applied to various types of equipment and issues
d. Aim for clarity and ease of use for individuals analyzing the data

Your task is to create a structured approach for analyzing these records, not to provide specific solutions. The goal is to develop a framework that can be easily applied and adapted by human analysts working with diverse equipment maintenance scenarios.

Here is an example record:
{{data}}
"""

boT = [meta_distiller_prompt]

distilled_prompt = """Use the following thought tempelate to anlyze the RECORD and provide distilled information:
1. Core Information Categories:
   a. Equipment Details: Manufacturer, model, type, and identifying information
   b. Reported Issues: Customer complaints or observed problems
   c. Technician Actions: Steps taken, diagnostics performed, and outcomes
   d. Parts Information: Required parts, availability, and ordering details
   e. Customer Information: Contact details, site information
   f. Follow-up Actions: Next steps, pending tasks, or escalations

2. Key Patterns and Indicators:
   a. Equipment Details: Recognize manufacturer names and model numbers.
   b. Reported Issues: Look for issue-specific terms (e.g., “doors not closing,” “custom made”).
   c. Technician Actions: Pay attention to sequences describing interactions with customers
   d. Parts Information: Words like "parts," "replace," "order," product numbers
   e. Follow-up Actions: Phrases like "need more info," "leaving so in continue"

3. Information Extraction Framework:
   Step 1: Scan for equipment details in structured fields and comments
   Step 2: Identify reported issues in comment fields
   Step 3: Extract technician actions and observations
   Step 4: Note any parts information or requirements
   Step 5: Create sections for each category (Equipment Details, Reported Issues, Technician Actions, Follow-Up Requirements).
   Step 6: Ensure that each category is clearly labeled and contains all relevant details.

4. Challenges and Considerations:
   - Inconsistent terminology or abbreviations across records, Solution: Use context clues and cross-reference with other records if possible.
   - Missing or incomplete information in some fields, Solution: Create a glossary of common terms and synonyms.
   - Multiple issues or actions described in a single comment, Solution: Break down the analysis into smaller batches.
   - Distinguishing between customer-reported and technician-observed issues
   - Identifying critical information buried in lengthy comments
   - Handling records with multiple updates or technician visits

RECORD: 
{{data}}
"""
extraction = """The goal is to create records that allows for efficient querying and analysis of resolved repair cases, enabling technicians to quickly find relevant information when dealing with similar issues in the future from DISTILLED_THOUGHT. If it has multiple issues and resolutions, extract more than one JSONs.
The fields are - manufacturer_name, manufacturer_number, model_number, issue_customer, issue_technician, resolved_item_no, resolved_item_description, equipment_type_description
Your output should be strictly in JSON: 
{
        "manufacturer_name": "LBC Bakery",
        "manufacturer_number": "LBE",
        "model_number": "LMO-MAX-G-LP",
        "issue_customer": "Pass thru cooler not cooling properly",
        "issue_technician": "Compressor running but not cooling; possible refrigerant leak",
        "resolved_item_no": "N/A",
        "resolved_item_description": "Installed new oven, Dormont hose, gas fittings, water line, and fittings. Assembled oven racks and set insulation."
        "equipment_type_description": "Convection Oven (Gas)"
}
DISTILLED_THOUGHT:
{{output[-1]}}
"""

distilled = [distilled_prompt, extraction]
convert_to_json_prompt = [extraction]
