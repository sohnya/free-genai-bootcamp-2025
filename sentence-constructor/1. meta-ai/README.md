
### Business goals
A chat agent that acts as a teaching assistant to guide students from translating a target English sentence into Japanese. The teaching assistant is not there to provide the direct answer, only guidance.

### Technical considerations

I use meta.ai (free version, no login) to test the prompts. 

I expect meta.ai to be not as good at reasoning as more powerful ChatGPT models, so I will use it as a first prompting tool. If I run into issues, I will use ChatGPT to refine the prompts. 

### Other considerations (Blocker)
meta.ai started by not giving the kanji/hiragana texts in the vocabulary table. Prompt iteration for that specific prompt:
1. The vocabulary used in the sentence, in Japanese. If there are Kanji, also write the pronunciation in Hiragana. 
2. The vocabulary used in the sentence, in Kanji/Hiragana/Katakana. If there are Kanji, also write the pronunciation in Hiragana. 
3. The vocabulary used in the sentence, in Kanji/Hiragana/Katakana. If there are Kanji, also write the it Hiragana inside paranthesis, e.g. 日本語(にほんご) 
After 3, meta said "I don’t understand Japanese yet, but I’m working on it. I will send you a message when we can talk in Japanese.". 

This led me to believe that the capabilities of the AI are limited, and I will move on to ChatGPT. 

### Summary of prompt iterations
1. **Initial Prompt (prompt-01)**
   - Basic structure with vocabulary table, sentence structure, and hints
   - Issues:
     - Hints contained irrelevant grammar information
     - Japanese vocabulary was output in Romaji instead of Kanji/Hiragana
     - No mechanism for revealing answers

2. **First Iteration (prompt-02)**
   - Improved structure with clear sections
   - Added explicit request for Kanji/Hiragana/Katakana in vocabulary
   - Made hint requirements more specific to the input sentence
   - Issues:
     - AI still output Japanese in Romaji
     - Inconsistent behavior when students asked for answers
     - Needed a better way to handle student requests for answers

3. **Second Iteration (prompt-03)**
   - Added "ICECREAM" keyword feature to reveal answers
   - Improved Kanji format with parenthetical Hiragana (e.g., 日本語(にほんご))
   - Reorganized vocabulary table format
   - Issues:
     - AI sometimes overwrote its answer and said it does not speak Japanese.
     - Inconsistent behavior with the ICECREAM keyword

