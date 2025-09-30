from sklearn.feature_extraction.text import TfidfVectorizer             #Turns words into numbers that a robot can understand
from sklearn.model_selection import train_test_split                    #Helps us split the data — some for teaching (training), some for testing
from sklearn.naive_bayes import MultinomialNB                           #A special robot that’s good at figuring out categories from words. (It's called a Naive Bayes classifier.)
from sklearn.metrics import accuracy_score , classification_report      #Accuracy_score and classification_report: These tell us how good our robot is at guessing

#Specific example, We use a small dataset of email text/labels (0 for not spam, 1 for spam)
emails = [
    # Spam (1)
    "Win a free iPhone now!",
    "Exclusive deal just for you! Limited time only!",
    "Congratulations! You've been selected for a $1000 gift card.",
    "Make money fast from home – no experience needed!",
    "Your loan is approved, click to claim!",
    "You've won a luxury vacation. Click to redeem.",
    "Get cheap meds now, no prescription required!",
    "This is not a scam – you’ve won!",
    "Act now! Only a few spots left for our seminar.",
    "You’ve been chosen! Claim your reward immediately.",
    "FREE trial for weight loss pills – act fast!",
    "Increase your income with zero effort!",
    "Cheap Rolex watches – 80% off!",
    "Get paid to take surveys. Start today!",
    "You've been pre-approved for a new credit card!",

    # Not Spam (0)
    "Can we reschedule our meeting to next week?",
    "Here are the notes from our last team call.",
    "Let me know your availability for the project demo.",
    "The invoice for this month is attached.",
    "Please find the requested files attached.",
    "Reminder: doctor's appointment tomorrow at 10 AM.",
    "Welcome to the team! Excited to have you onboard.",
    "Your Amazon order has been shipped.",
    "Let's have lunch next Tuesday.",
    "Happy birthday! Hope you have a great day.",
    "Don't forget to submit your timesheet.",
    "Here is the draft for the upcoming article.",
    "Team outing scheduled for Friday afternoon.",
    "Check out the updated project timeline.",
    "Looking forward to your feedback on the proposal."
]

labels = [
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,  #15 spam
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0   #15 not spam
]
#1 = spam
#0 = not spam

#Robots don’t understand words like "money" or "gift", so we need to turn the words into numbers
#Convert text data into numerical features using Count vectorization:
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(emails)

#Split into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(
    x, labels, test_size=0.2, random_state=42
)
#X_train: the emails the robot will learn from
#y_train: the labels (spam or not spam) for those emails
#x_test: the emails to test the robot
#y_test: the real answers for those test emails
#test_size=0.2 means 20% of emails are saved for testing, 80% for training

#You're making a Naive Bayes spam detector, and teaching it using the training data
#Create a multinominal Naive Bayes classifier:
model = MultinomialNB()
#Train the model on training data:
model.fit(X_train, y_train)

#This makes the robot guess if the test emails are spam or not
#Make prediction on test data:
y_pred = model.predict(X_test)

#Evaluate the model:
accuracy = accuracy_score(y_test, y_pred)           #Accuracy: how many guesses it got right.
report = classification_report(y_test, y_pred)      #Classification report: gives you more details like precision and recall.

print("🔎 Accuracy:", round(accuracy * 100, 2), "%")
print("🧾 Classification Report:\n", report)

#Predict wether a new email is spam or not:
new_email = ["Congratulations, you have been selected for a cruise!"]
new_email_vectorized = vectorizer.transform(new_email)
predicted_label = model.predict(new_email_vectorized)

if predicted_label[0] == 0:
    print(f"Predicted not as spam.")
else:
    print(f"Predicted as spam.")
    

#How it predicts the result:
#From the emails we inserted earlier, it learns that words like:
#Win, free, gift, click - Are often labeled as spam.

#Review, Meet, Document - Are often not spam.
