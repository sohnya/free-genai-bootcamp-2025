# GenAI Bootcamp

This is my repo for the [FREE GenAI Bootcamp](https://genai.cloudprojectbootcamp.com/), where I explore and compare different AI approaches to teaching Japanese to beginner language learners. 

## Japanese Sentence Constructor - AI Assistant Comparison
`sentence-contructor` contains an example of iterative work in generating prompts to create a Japanese teaching assistant. The prompts are fed into an AI Assistant (meta.ai, ChatGPT) and the output is reviewed by a human to build the next prompt in the series. 

### Github Link to Sentence Constructor
https://github.com/sohnya/free-genai-bootcamp-2025/tree/main/sentence-constructor

### Github Link to GenAI Architecture


### Hypothesis and Technical Uncertainty
- Free AI Assistants are limited to less performant models, and they will likely not give as good answers are Pro versions of more powerful models.
- It might not be possible to build a reasonable Japanese language teaching assistant using only AI Assistants. There will be some domain knowledge that will need to be captured in the prompts. I will see how far I can go with my limited knowledge and Japanese and limited grammar knowledge.
- The AI might forget what I told it in the inial prompt or make up a word that doesn't exist in the sentence. It might not be a good translator. 

### Technical Exploration
Briefly describe the path of technical exploration during these projects.
- Creating examples using more powerful (Claude 3.5 Sonnet on Windsurf) to make sure that they are correct. Manually validating the examples given and tweaking some outputs (such as mapping です to be a verb instead "copula").  
- Quick testing of different prompt structures and iteration/refinement of prompts
- Analyzing the feedback from AI responses
- Low technical overhead for testing new features (like the ICECREAM keyword for revealing an answer)
- Exploring different prompting techniques, mainly related to how output should be presented/structured (1. Vocabulary 2. Sentence Structure 3. Hints in markdown format), what answers are correct/incorrect (using examples). 
- Increasingly specific prompts to tell the AI how to be a good translator, e.g. not adding/removing vocabulary. 

### Final Outcomes
Describe your final outcomes or domain knowledge acquired.

- Not all LLMs are the same, the comparison of different assistants (and thereby, models) increased my understanding of limitations and capabilities of models. If we want to get the most accurate answers, we usually need to use paid versions of AI Assistants. If I had to use locally deployed models, I don't believe I would've been able to create a "reasonable" Japanese teacher in such a short time. 
- Testing of different prompt structures and iteration/refinement of prompts enable rapid prototyping of applications. This leads to low technical overhead for testing new features (like the ICECREAM keyword for revealing an answer). 
- Prompting techniques discovered while working with AI-Powered Assistants are
-- using examples to guide output format
-- implementing "secret" keywords for shortcuts
-- creating structured sectioning of responses. 
The main driver for improvements in output was adding more complex examples.
- AI Assistants are not reliable translators, it takes domain knowledge and extensive testing to implement a "reasonable" Japanese teacher.
