from ..authenticate.models import CredentialsOpenAI
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


def track_template_versions(template):
    from .models import TemplateAIVersion
    last_version = TemplateAIVersion.objects.filter(template__id = template.id).order_by('-created_at').first()
    number = 1 if last_version is None else last_version.number + 1
    new_version = TemplateAIVersion.objects.create(template=template, number=number, body=template.prompt)
    new_version.save()




def execute_a_template(template, user_input, user):
    api_key = CredentialsOpenAI.objects.filter(user=user).first()
    chat = ChatOpenAI(temperature=0, openai_api_key=api_key.token)
    
    system_message_prompt = SystemMessagePromptTemplate.from_template(template.prompt)
    example_human = HumanMessagePromptTemplate.from_template(template.human_example)
    example_ai = AIMessagePromptTemplate.from_template(template.ai_example)
    human_template="{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, example_human, example_ai, human_message_prompt])
    chain = LLMChain(llm=chat, prompt=chat_prompt)
    return chain.run(user_input)