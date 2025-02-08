
### Business goals
A chat agent that acts as a teaching assistant to guide students from translating a target English sentence into Japanese. The teaching assistant is not there to provide the direct answer, only guidance.

### Technical considerations
I use ChatGPT 4o (pro, paid version) to refine prompts based on meta.ai prompts. 

To make the comparison fair, I added a specific prompt to make sure the AI does not use existing chats as input context.

### Prompt iteration overview

1. **Prompt-03**: Initial prompt setup with basic teaching assistant role and vocabulary table format. Included ICECREAM keyword feature for answer reveal.

2. **Prompt-04**: Added clarification about vocabulary handling. Main issues:
   - Missing 好き in vocabulary
   - Incorrect sentence structure representation
   - Unnecessary use of ⭕️/❌ symbols

3. **Prompt-05**: Major improvements:
   - Added comprehensive list of particles to exclude
   - Specified that vocabulary words should be lowercase unless names
   - Added clarification about particle exclusion
   - Added examples of sentence structures
   - Added Japanese-specific considerations (私 usage, ⭕️/❌ usage)

4. **Prompt-06**: Refined the prompt with example sentences and structures.

5. **Prompt-07**: Enhanced with more complex example sentences while maintaining beginner level:
   - Added proper word class breakdowns
   - Included arrow notation for sentence structure
   - Demonstrated handling of compound sentences

6. **Prompt-08**: Further refinements to ensure consistent format and clearer instructions.
