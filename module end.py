feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya',
             'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and Poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}
n = int(input("How many feedbacks do you want to add? "))
for i in range(n):
    name = input("Enter name: ")
    feedback = input("Enter feedback: ")
    rating = int(input("Enter rating (1-5): "))
    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)
    print(feedback_data)

for i in range(len(feedback_data['Feedback'])):
    feedback = feedback_data['Feedback'][i]
    
    feedback = feedback.replace('.','')
    feedback = feedback.replace(',','')
    feedback = feedback.replace('!','')
    feedback = feedback.replace('?','')
    feedback = ' '.join(feedback.split())
    feedback = feedback.lower()
    
    feedback_data['Feedback'][i] = feedback
    print(feedback_data['Feedback'])

def count_word_in_feedbacks(word):
    count = 0
    for feedback in feedback_data['Feedback']:
        if word.lower() in feedback.lower().split():
           count +=1
    return count
print("Good :", count_word_in_feedbacks("good"))

print("Poor:", count_word_in_feedbacks("poor"))
print("Exellent:", count_word_in_feedbacks("excellent"))
print("Final Feedback Data:")
print(feedback_data)
average = sum(feedback_data['Rating'])/len(feedback_data['Rating'])
print("Average Rating:", average)
longest = max(feedback_data['Feedback'], key=lambda x: len(x.split()))
print("Longest Feedback:", longest)
print("WORD Count:", len(longest.split()))
unique_words = set()

for feedback in feedback_data['Feedback']:
            for word in feedback.split():
                unique_words.add(word)
print("Unique Words:", sorted(unique_words))

sorted_feedbacks = sorted(
            zip(feedback_data['Name'], feedback_data['Feedback'],
                feedback_data['Rating']),
            key=lambda x: x[2],
            reverse=True
)            
print("Feedbacks Sorted by Rating:")
for item in  sorted_feedbacks:
    print(item)

                                 
