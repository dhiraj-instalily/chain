import os
from typing import List, Dict, Union
from dotenv import load_dotenv
from chain import MinimalChainable
import llm
from prompts_library import *
DEFULT_PROMPTS = [
            # prompt #1
            "Generate one blog post title about: {{topic}}. Respond in strictly in JSON in this format: {'title': '<title>'}",
            # prompt #2
            "Generate one hook for the blog post title: {{output[-1].title}}",
            # prompt #3
            """Based on the BLOG_TITLE and BLOG_HOOK, generate the first paragraph of the blog post.
BLOG_TITLE:
{{output[-2].title}}
BLOG_HOOK:
{{output[-1]}}""",
        ]

def build_models():
    load_dotenv()

    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    sonnet_3_5_model: llm.Model = llm.get_model("claude-3.5-sonnet")
    sonnet_3_5_model.key = ANTHROPIC_API_KEY

    return sonnet_3_5_model


def prompt(model: llm.Model, prompt: str):
    res = model.prompt(
        prompt,
        temperature=0.5,
    )
    return res.text()


def prompt_chainable_poc():

    sonnet_3_5_model = build_models()

    result, context_filled_prompts = MinimalChainable.run(
        context={"topic": "AI Agents"},
        model=sonnet_3_5_model,
        callable=prompt,
        prompts=DEFULT_PROMPTS,
    )

    chained_prompts = MinimalChainable.to_delim_text_file(
        "poc_context_filled_prompts", context_filled_prompts
    )
    chainable_result = MinimalChainable.to_delim_text_file("poc_prompt_results", result)

    print(f"\n\n📖 Prompts~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n{chained_prompts}")
    print(f"\n\n📊 Results~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n{chainable_result}")

    pass

def parts_predictor(prompts, context):

    sonnet_3_5_model = build_models()

    result, context_filled_prompts = MinimalChainable.run(
        context=context,
        model=sonnet_3_5_model,
        callable=prompt,
        prompts=prompts,
    )

    chained_prompts = MinimalChainable.to_delim_text_file(
        "poc_context_filled_prompts", context_filled_prompts
    )
    chainable_result = MinimalChainable.to_delim_text_file("poc_prompt_results", result)

    print(f"\n\n📖 Prompts~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n{chained_prompts}")
    print(f"\n\n📊 Results~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n{chainable_result}")

    pass

def main(prompts=None, context=None):

    # prompt_chainable_poc()
    parts_predictor(prompts, context)


if __name__ == "__main__":
    main()