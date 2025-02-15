#!/bin/bash

echo "Testing API endpoints..."

echo -e "\n1. Get all words (default sorting):"
curl -s "http://localhost:8000/v1/words" | jq

echo -e "\n2. Get words sorted by kanji:"
curl -s "http://localhost:8000/v1/words?sort_by=kanji&order=desc" | jq

echo -e "\n3. Get all groups:"
curl -s "http://localhost:8000/v1/groups" | jq

echo -e "\n4. Get words from group 1:"
curl -s "http://localhost:8000/v1/groups/1" | jq

echo -e "\n5. Create new study session:"
SESSION_RESPONSE=$(curl -s -X POST "http://localhost:8000/v1/study_sessions" \
  -H "Content-Type: application/json" \
  -d '{"group_id": 1, "study_activity_id": 1}')
echo $SESSION_RESPONSE | jq
SESSION_ID=$(echo $SESSION_RESPONSE | jq -r '.id')

echo -e "\n6. Log a review for word 1 in the session:"
curl -s -X POST "http://localhost:8000/v1/study_sessions/$SESSION_ID/review" \
  -H "Content-Type: application/json" \
  -d '{"word_id": 1, "correct": true}' | jq

echo -e "\n7. Get words sorted by kanji:"
curl -s "http://localhost:8000/v1/words?sort_by=kanji&order=desc" | jq 