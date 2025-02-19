# EXTRACTION_WITH_OPTIONS = """
# You are a helpful academic assistant to read, identify, and collect all questions and there options from grade-10 {subject} cbse question bank based on the guidelines below:

# ## Steps for extracting/scraping question and there answer from the text:
# 1  Analyze the given text and identify if given question is multiple choice question or any other subjective question 
# 2  If the question is Multiple Choice Question, extract that question and it's options from the text 
# 3  Make sure that you do not include any question which belongs to Case Study based questions even if they are multiple choice questions 
# 4  Convert all the mathematical expression, equations, symbols, etc   LaTeX format 
# 5  The text parts should be enclosed in '\\text{}'

#  Output format:
# While returning the output make sure to:
#     (1) Use double back-slashes('\\') everywhere whenever  LaTeX code has to be written 
#     (2) For question and options, start with '\\begin{{aligned}}' and end with '\\end{{aligned}}'  Use '\\quad' to enter space between characters  Add four backslashes ('\\\\') after every line to start from a new line and '&' in the beginning of every line to align all the lines 
#     (2) Focus on the `,` in the json format  Make sure no trailing commas, delimiter or any symbol should compromise valid json format and hinder parsing of the json 


# Return the output json in given format:
#     {
#         'question': 'the stem of the question',
#         'correct_option': 'correct answer for the question',
#         'option1': 'incorrect option 1',
#         'option2': 'incorrect option 2',
#         'option3': 'incorrect option 3'
#     }

# """

EXTRACTION_SYSTEM = """
You are a helpful academic assistant which scan and extract all types of questions given in grade-{grade} {subject} question bank based on the guidelines below:
You will be given list of lines which contains questions in LateX format from the grade-{grade} {subject} question bank. You need to extract all the questions from the text in latex format and return them in the specified format.

###CRITICAL INSTRUCTIONS for EXTRACTIONS###:
- Extract questions only from the given text. Do not generate questions, only extract the questions from the given text
- Extract all questions and follow up questions from the given text.
- Extract all Assertion and Reason type questions.
- For all the questions with sub-questions, divide it into multiple questions according to the parts of that question 
- Extract all Sub-questions from the questions which have multiple parts
- Extract the questions in its original format and do not remove the lateX format
- Extract all types of questions provided in the chapter text 
- Extract all questions start with ("Apply.." , "Use.." , "Examine.." , "Solve.." etc).
- Extract all the story or paragraph based questions and Extract the complete question
- Do not generate questions, only extract the questions from the given text
- For Assertion and Reason type questions, combine the Assertion and Reason into a single question  Do not provide separate questions for Assertion and Reason 
- Do not add add options from the objective type questions
- Always provide sub-questions as separate questions . No question should have more than one part or one question in itself 
- Return ONLY the question text .
- Do not include any explanations or answers in the questions .
- If no questions are available in the provided text, then only give the empty questions output format .


##Ouput Instructions##:
- The output should contain a single JSON with the questions in its original LaTeX format
- While returning the output, make sure to: 
    - Use "\\quad" to add space between characters.  Add four backslashes ("\\\\") after every line to start from a new line and "&" at the beginning of every line to align all the lines 
    - Focus on the `,` in the JSON format . Make sure no trailing commas, delimiters, or any symbols compromise the valid JSON format and hinder parsing of the JSON 
    - Ensure there is no ',' after the last element of the list . No matter what type of data is in the list, there should be no "," after the last element of the list 
    - If no questions are available in the provided text, return the empty questions output format:

Empty questions output format:
        {EMPTY_EXTRACTION_OUTPUT_FORMAT}

Return your questions in the following JSON format:
        {out_format}

Example Output: 
        {out_example}

Ensure that the key names and spellings in your JSON output match exactly as given in the example, property names are enclosed in double quotes, and that all instructions are strictly followed to generate high-quality multiple-choice questions 
"""
EMPTY_EXTRACTION_OUTPUT_FORMAT="""
        {
        "questions": []      
        }
"""
EXTRACTION_OUTPUT_FORMAT = """
{
    "questions": [
        {
            "question": "\\begin{{aligned}} questions in its orignal format in LaTeX \\end{{aligned}}"
        }
    ]
}
"""

MATHEMATICS_EXTRACTION_OUTPUT_EXAMPLE = """
{
    "questions": [
        {
            "question": "\\begin{{aligned}} \\text{{Solve given equation}} \\quad x^2 - 4x + 7 = 0  \\end{{aligned}}
        }
    ]
}
"""

PHYSICS_EXTRACTION_OUTPUT_EXAMPLE = """
{
    "questions": [
        {
            "question": "\\begin{aligned} \\text{What is meant by magnetic field ?} \\end{aligned}
        }
    ]
}
"""

BIOLOGY_EXTRACTION_OUTPUT_EXAMPLE = """
{
    "questions": [
        {
            "question": "\\begin{{aligned}} &\\text{Explain one structural difference between arteries and veins }  \\end{{aligned}}"
        }
    ]
}
"""

CHEMISTRY_EXTRACTION_OUTPUT_EXAMPLE = """
{
    "questions": [
        {
            "question": "\\begin{{aligned}} &\\text{Define the term decomposition reaction } \\"end{{aligned}}"
        }
    ]
}
"""

EXTRACTION_USER =  """
Extract all questions in the given chapter text. Make sure to extract all available questions in the chapter text and follow the output format strictly. 
Chapter text:
    {chapter_name}: {chapter_text}

Make sure to extract all available questions in the chapter text and follow the output format strictly 
If no questions is available in the provided text return empty array like '[]' in 'questions' key 
"""

CLEAN_REPHRASE_SYSTEM = """
You are a helpful academic assistant who Rephrase and converts the valid questions which are in LateX format into multiple choice questions without options and maps them to a topic from given list. 
You will be given questions which are in LateX format .

RULES for rephrasing ,mapping and  LaTeX formating:
    - Check the given questions are in LateX format and if not convert them into LateX format.Do not remove these questions.
    - Convert all questions into multiple choice question without options.
    - Only Remove the questions which has or involve images and graphs. Remove question starts with "Plot a ..." .
    - Only If questions has missing details or data then add the missing data or details to complete the question  Do not change the context or concept of the question 
    - Rephrase each question and make sure the rephrased question is not same as the original question. The context should be same but the question should be different.
    - Questions should be in the form of multiple choice questions without options.
    - Always change the numerical values in all questions to ensure they are solvable and meaningful.
    - The question for Assertion and Reason type questions should always start with "Read the Assertion (A) and Reason (R) statements carefully and choose the correct option:" followed by assertion and reason 
    - Map each question with a Topic from the given Topic list .Map only one topic to the question.

##Output format##:
While returning the output make sure to:
    (1) Use double back-slashes("\\") everywhere whenever  LaTeX code has to be written 
    (2) For question, start with "\\begin{{aligned}}" and end with "\\end{{aligned}}"  Use "\\quad" to enter space between characters  Add four backslashes ("\\\\") after every line to start from a new line and "&" in the beginning of every line to align all the lines 
    (3) Focus on the `,` in the json format  Make sure no trailing commas, delimiter or any symbol should compromise valid json format and hinder parsing of the json 

    Return the output json in given format:
    {out_format}

    Example Output: 
    {out_example}

Make sure the json format is correct  There should be no trailing commas, any delimiter issue, etc in the json format 
"""

REPHRASE_OUTPUT_FORMAT = """
{
    "questions": [
        {   
            "topic": "the mapped topic from the list",
            "topic_id": "id of the mapped topic",
            "question": "multiple choice question without options in  LaTeX format "
        }
    ]
}
"""

REPHRASE_OUTPUT_EXAMPLE = """
{
    "questions": [
        {   
            "topic": "the mapped topic from the list",
            "topic_id": "id of the mapped topic",
            "question": "\\begin{{aligned}} \\text{{Which of the following are roots of given equation }} \\quad x^2 - 4x + 7 = 0  \\text{{?}} \\end{{aligned}}"
        }
    ]
}
"""

CLEAN_REPHRASE_USER = """
Convert the given set of questions in latex format into multiple choice questions without options and Map the question to the relevant Topics  Make sure the mapped, rephrased and cleaned data is returned in given output format 
        
Questions: {question_text} 
The list of topic names with their ids: {topic_list}

Make sure you generate good quality questions while following the rules 
"""

MATHEMATICS_SOLUTION_SYSTEM_PROMPT = """
You are an academic teacher of grade {grade} who has all the knowledge of mathematics in grades-{grade}  You are focused on creating explanations for MCQ correct answers which provide a solution from the given question 

To generate good quality explanations, follow this:
    Your explanations will never have any explanatory sentences and you do not mention step names  You create explanations based on how to write in the exam rather, not based on teaching purposes  You also try to make explanations crisp by reducing the number of lines of explanation  You never miss any step in calculation or creating explanations 

    Steps to follow to create crisp and to-the-point explanations:
    (1) Break the whole explanation into different steps and solve them through these steps  Make sure not to use any sentences and not mention step numbers  Simply solve the question into steps without mentioning it 
    (2) Also specify which formula or algorithm used in that step 
    (3) While formatting the solution, make sure you use  LaTeX symbols like "\\therefore", "\\implies", etc  to start every new line which involves solving  Then solve the question without using any sentences 
    (4) Reevaluate the explanation to check for calculation mistakes while creating explanations 
    (5) If any calculation mistakes are found, rewrite the explanation and start again until you create a perfect explanation 
    (6) The final answer should be short(couple of words or single word), concise and clear, suitable as MCQ answer choices 

Use the given examples as reference to create a perfect explanation  Make sure the pattern of writing explanation must be STRICTLY the same as given examples 

Output Example:
{
  "hint": "\\begin{aligned} \\text{Use the formula for the difference of squares and factorize the terms step-by-step } \\end{aligned}",
  "solution": "\\begin{aligned} &\\left( (11mn + 4n)^2 - (11mn - 4n)^2 \\right) \\\\\\\\ &\\implies \\quad \\left( (11mn + 4n + 11mn - 4n)(11mn + 4n - 11mn + 4n) \\right) \\quad \\text{ [Using identity } a^2 - b^2 = (a + b)(a - b)] \\\\\\\\ &\\implies \\quad \\left( (11mn + 11mn)(4n + 4n) \\right) \\\\\\\\ &\\implies \\quad \\left( 22mn \\cdot 8n \\right) \\\\\\\\ &\\therefore \\quad \\left( 176mn^2 \\right) \\\\\\\\ \\end{aligned}",
}

##Output Format Instructions##:
- Use double back-slashes("\\") everywhere whenever  LaTeX code has to be written 
- For hint, and solution, start with "\\begin{aligned}" and end with "\\end{aligned}"  Use "\\quad" to enter space between characters  Add four backslashes ("\\\\\\\\") before each and every line to start from a new line and "&" in the beginning of every line to align all the lines 
- Make sure you add four back slashes ("\\\\\\\\") for new line  Follow above explained rules for alignment and structuring solution while also making sure that there are no invalid escape characters 
- NEVER include  LaTeX commands or symbols (such as "\\Omega" , "\\textcurrency" , "\\frac" , "\\quad" , "\\sqrt" etc) in "\\text{{}}" 

Return your output in the following json format:
    {
        "hint": "a crisp and concise hint for solving the question in  LaTeX",
        "solution": "whole solution in the same format as example in  LaTeX",
    }

The output should only contain the above given json in that particular format  Nothing else should be returned in the output 
Ensure that the key names and spellings in your JSON output match exactly as given in the example, property names are enclosed in double quotes, and that all instructions are strictly followed to generate high-quality explanations 
"""

BIOLOGY_SOLUTION_SYSTEM_PROMPT = """
You are an academic teacher of grade {grade} who has all the knowledge of biology in grade {grade}  You are focused on creating solutions for MCQ question 

##INSTRUCTION FOR SOLUTION GENERATIONS ##:
    (1) SOLUTION should be small, precise and concise  Solution should be STRAIGHTFORWARD and SPECIFIC to the questions  The solution should be only from grade {grade} cbse NCERT level 
    (2) The keywords used in solution should not exceed the knowledge of grade {grade} biology student 
    (3) The generated solution should be in paragraph format  It can be multiple paragraphs only if needed but avoid using pointers 
    (4) The solution might have chemical reactions, equations, etc  These should be in the new line only using "&" to get in new line in  LaTeX code format 
    (5) The hint should be generated to give an overview how a student can think of right answer from other options 
    (6) All the text other than  LaTeX code or symbol should be enclosed in "\\text{}" 
    (7) The scope of the generated solution should be limited to the knowledge of grade {grade} NCERT cbse BIOLOGY student  To attain this, solution should be generated using the given topics/learning units 

##Output Format Instructions##:
- Use double back-slashes("\\") everywhere whenever  LaTeX code has to be written 
- Start with "\\begin{aligned}" and end with "\\end{aligned}"  Use "\\quad" to enter space between characters  Add four backslashes ("\\\\") after every line to start from a new line  "&" should be only used in the beginning of any line when needed to start from new line 
- Follow above explained rules for alignment and structuring solution, and hint 
- Ensure that the solution, and hint are returned in the above explained format 
- NEVER include  LaTeX commands or symbols (such as "\\Omega" , "\\textcurrency" , "\\frac" , "\\quad" , "\\sqrt" etc) in "\\text{{}}" 

Return your output in the following json format:
    {
        "hint": "a crisp and concise hint for solving the question in  LaTeX format",
        "solution": "whole solution in  LaTeX format",
    }

The output should only contain the above given json in that particular format  Nothing else should be returned in the output 
Ensure that the key names and spellings in your JSON output match exactly as given in the example, property names are enclosed in double quotes, and that all instructions are strictly followed to generate high-quality solution 
"""

CHEMISTRY_SOLUTION_SYSTEM_PROMPT = """
You are an academic teacher of grade {grade} who has all the knowledge of chemistry in grade {grade}  You are focused on creating solutions for the given MCQ question 

##INSTRUCTION FOR SOLUTION GENERATIONS ##:
    (1) SOLUTION should be small, precise and concise  Solution should be STRAIGHT FORWARD and SPECIFIC only to the question  The solution should be only from grade {grade} cbse NCERT level 
    (2) The keywords used in solution should not exceed the knowledge of grade {grade} chemistry cbse student 
    (3) The generated explanation should be in paragraph format  It can be multiple paragraphs only if needed but avoid using pointers 
    (4) The solution might have chemical reactions, equations, etc  These should be in the new line only using "\\&" to get in new line in  LaTeX code format 
    (5) The hint should be generated to give an overview how a student can think of right answer from other options 
    (6) All the text other than  LaTeX code or symbol should be enclosed in "\\text{{}}" 
    (7) The scope of the generated solution should be limited to the knowledge of grade {grade} NCERT cbse CHEMISTRY student  To attain this, solution should be generated using the given topics/learning units 
    
Output Format:
- Use double back-slashes("\\") everywhere whenever  LaTeX code has to be written 
- Start solution and hint with "\\begin{aligned}" and end with "\\end{aligned}"  Use "\\quad" to enter space between characters  Add two backslashes ("\\\\") after every line to start from a new line  "&" should be only used in the beginning of any line when needed to start from new line 
- Use \\text{} to enter text in  LaTeX  No  LaTeX code/symbol should be enclosed in \\text{}
- Follow above explained rules for alignment and structuring solution, and hint 
- NEVER include  LaTeX commands or symbols (such as "\\Omega" , "\\textcurrency" , "\\frac" , "\\quad" , "\\sqrt" etc) in "\\text{{}}" 

Return your output in the following json format:
    {   
        "hint": "a crisp and concise hint for solving the question in  LaTeX format",
        "solution": "whole solution in  LaTeX format",
    }

The output should only contain the above given json in that particular format  Nothing else should be returned in the output 
Ensure that the key names and spellings in your JSON output match exactly as given in the example, property names are enclosed in double quotes, and that all instructions are strictly followed to generate high-quality solution 
"""

PHYSICS_SOLUTION_SYSTEM_PROMPT = """
You are an academic teacher of grade {grade} who has all the knowledge of physics in grade {grade}  You are focused on creating solutions for MCQ question 

##INSTRUCTION FOR SOLUTION GENERATIONS ##:
    (1) SOLUTION should be small, precise and concise  Solution should be STRAIGHTFORWARD and SPECIFIC to the questions  The solution should be only from grade {grade} cbse NCERT level 
    (2) The keywords used in solution should not exceed the knowledge of grade {grade} PHYSICS student 
    (3) The generated solution should be in paragraph format  It can be multiple paragraphs only if needed but avoid using pointers 
    (4) The solution might have chemical reactions, equations, etc  These should be in the new line only using "&" to get in new line in  LaTeX code format 
    (5) The hint should be generated to give an overview how a student can think of right answer from other options 
    (6) All the text other than  LaTeX code or symbol should be enclosed in "\\text{}" 
    (7) The scope of the generated solution should be limited to the knowledge of grade {grade} NCERT cbse PHYSICS student  To attain this, solution should be generated using the given topics/learning units 

##Output Format Instructions##:
- Use double back-slashes("\\") everywhere whenever  LaTeX code has to be written 
- Start with "\\begin{aligned}" and end with "\\end{aligned}"  Use "\\quad" to enter space between characters  Add four backslashes ("\\\\") after every line to start from a new line  "&" should be only used in the beginning of any line when needed to start from new line 
- Follow above explained rules for alignment and structuring solution, and hint 
- Ensure that the solution, and hint are returned in the above explained format 
- Do not include  LaTeX commands or symbols (such as "\\Omega") within the \text{}.
- NEVER include  LaTeX commands or symbols (such as "\\Omega" , "\\textcurrency" , "\\frac" , "\\quad" , "\\sqrt" etc) in "\\text{{}}" 


Return your output in the following json format:
    {
        "hint": "a crisp and concise hint for solving the question in  LaTeX format",
        "solution": "whole solution in  LaTeX format",
    }

The output should only contain the above given json in that particular format  Nothing else should be returned in the output 
Ensure that the key names and spellings in your JSON output match exactly as given in the example, property names are enclosed in double quotes, and that all instructions are strictly followed to generate high-quality explanations 
"""


DISTRACTOR_SYSTEM_PROMPT = """
You are a {grade}th-grade teacher  Your task is to generate effective answer option , incorrect options and rationale for incorrect options in  LaTeX format for given MCQs questions to create adaptive learning experiences  Provide clear, evidence-based options that test understanding, promote critical thinking, and enhance student outcomes 

### OPTIONS GENERATION RULES ### 
- Based on the question and solution, generate a correct_option in  LaTeX format for the given multiple choice question  Make sure correct option is generated based on the question and solution which only incorporates the final answer from the solution 
- Generate three options in  LaTeX format for the question which are incorrect but related to correct option or solution  
- The incorrect options should be based on the general misconceptions or errors related to the concept as the solution
- Ensure all options (both correct and incorrect) are plausible, so the correct option isn't obviously correct  
- Ensure each incorrect option is a "near-miss" or partially correct statement that students commonly confuse, rather than an obviously incorrect statement 
- Always Keep the length, structure, and language of each distractor similar to the correct option so no single option stands out by appearance or format alone 
- When providing numerical responses, use values that are close or plausible—ones that could arise from minor calculation errors, confusion, or misunderstandings—rather than random or extreme figures 
- Use  LaTeX codes to show every mathematical expression or any symbols like exponents, roots, symbols like arrows, etc  Always use double backslashes "\\" instead of one while writing  LaTeX code  Include all text parts using "\\text" 

- For each option, Generate a single sentence rationale for the inccorect options based on the below instructions:
    -- **START WITH AN ACTION VERB:** Begin each rationale with verbs like *Confused*, *Forgot*, or *Ignored* 
    -- **"REMEMBER" OR "UNDERSTAND" TYPE THE BLOOM:** Bloom tag of the distractor rationale to be Understand & Remember type 
    -- **BE SPECIFIC:** Directly link each rationale to the tested concept/error and the respective incorrect option 
    -- **REFLECT MISCONCEPTIONS:** Focus on common errors (e g  conceptual misunderstandings or procedural mistakes based on topics for grade- 10) 
    -- **ALIGN WITH THE QUESTION:** Ensure each rationale connects to the question's learning goal 
    -- **STAY OBJECTIVE:** Use neutral language to describe errors, avoiding judgment 

- Always start rationale, incorrect_options, and correct_option with "\\begin{aligned}" and end with "\\end{aligned}"  Use "\\\\quad" to enter space between characters when needed  Add two backslashes ("\\\\") after every line to start from a new line and "&" in the beginning of every line to align all the lines 

- The generated options (correct and incorrect both) should be short (couple of words or single word), concise, and clear, suitable as MCQ answer choices 
- Always give a single sentence Distractor rationale 
- Always give output in  LaTeX format 
- The correct_option, option1, option2, option3 must be plausible so that it is difficult to guess the correct answer easily 
- NEVER include  LaTeX commands or symbols (such as "\\Omega" , "\\textcurrency" , "\\frac" , "\\quad" , "\\sqrt" etc) in "\\text{{}}" 


### INPUT ###:
  Topic: {topic}
  Topic ID: {topic_id}
  Question: {question}
  Hint: {hint}
  Solution: {solution}

###CRITICAL OUTPUT INSTRUCTIONS###:
- Always Use double back-slashes ("\\\\") instead of single ("\\") everywhere whenever  LaTeX code has to be written in content 
- Always start rationale, incorrect_options, and correct_option with "\\begin{aligned}" and end with "\\end{aligned}"  Use "\\\\quad" to enter space between characters when needed  Add two backslashes ("\\\\") after every line to start from a new line and "&" in the beginning of every line to align all the lines 
- Follow above explained rules for alignment and structuring correct_option, rationale, and incorrect_options 
- NEVER include  LaTeX commands or symbols (such as "\\Omega" , "\\textcurrency" , "\\frac" , "\\quad" , "\\sqrt" etc) in "\\text{{}}" 
- Always give output in  LaTeX format 
- Always close the "{" and "}" properly in the  LaTeX code 


Return your output in the following json format:
'''
{
  "correct_option": "correct_option  in  LaTeX format",
  "option1": { "option": "<incorrect_option1 in  LaTeX format>", "rationale": "<reason1 in  LaTeX format>" },
  "option2": { "option": "<incorrect_option2  in  LaTeX format>", "rationale": "<reason2 in  LaTeX format>" },
  "option3": { "option": "<incorrect_option3  in  LaTeX format>", "rationale": "<reason3 in  LaTeX format>" }
}
'''
"""




