import google.generativeai as genai
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

genai.configure(api_key=settings.GEMINI_API_KEY)

def load_system_prompts():
    with open("prompts/unihelp_template.md" , "r" , encoding="utf-8") as f:
        return f.read()
    


@api_view(["POST"])
def chat_with_unihelp(request):
    try:
        SYSTEM_TEMPLATE = load_system_prompts()
        user_message = request.data.get("message","")

        full_prompt = f"""
          {SYSTEM_TEMPLATE}

          User: {user_message}
          AI:

         """
        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(
            full_prompt,
            generation_config={
                "temperature" : 0.4 ,
                "max_output_tokens": 600
            }
        )

        return Response({
            "response":response.text
        })
    
    except Exception as e:
        return Response({
            "error": str(e)
        },status=500)