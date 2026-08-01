import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = {
    "message": [
        # ---------------- Spam ----------------
        "Win money now",
        "Free lottery ticket",
        "Claim your prize",
        "Congratulations you won cash",
        "Click here to claim reward",
        "Limited time offer buy now",
        "Exclusive deal just for you",
        "You have won a free vacation",
        "Urgent claim your bonus",
        "Earn dollars from home",
        "Congratulations you are selected",
        "Free recharge available",
        "Win an iPhone today",
        "Get cashback instantly",
        "Lucky winner claim now",
        "Lowest price guaranteed",
        "Click the link to receive gift",
        "You have been chosen",
        "Special promotion ends today",
        "Act now to win rewards",
        "Get free coupons",
        "Claim your Amazon gift card",
        "You won a cash prize",
        "Free movie tickets available",
        "Exclusive reward waiting",

        # ---------------- Not Spam ----------------
        "Meeting at 10 AM",
        "Project submission tomorrow",
        "Happy Birthday",
        "Team meeting today",
        "Homework submission",
        "Let's have lunch together",
        "Call me when you arrive",
        "Can you send me the notes",
        "See you in class tomorrow",
        "The assignment deadline is Friday",
        "Don't forget the meeting",
        "Please review the document",
        "Dinner is ready",
        "Your order has been delivered",
        "Good morning have a nice day",
        "Let's play cricket this evening",
        "The exam starts at 9 AM",
        "Your package is out for delivery",
        "Please attend today's lecture",
        "I will call you later",
        "Can we reschedule the meeting",
        "The train arrives at 6 PM",
        "Best wishes for your interview",
        "Thank you for your help",
        "Please submit your report"
    ],

    "spam": [
        # 25 Spam
        1,1,1,1,1,
        1,1,1,1,1,
        1,1,1,1,1,
        1,1,1,1,1,
        1,1,1,1,1,

        # 25 Ham
        0,0,0,0,0,
        0,0,0,0,0,
        0,0,0,0,0,
        0,0,0,0,0,
        0,0,0,0,0
    ]
}
df = pd.DataFrame(data)

X = df["message"]
y = df["spam"]

x_train , x_test , y_train , y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)
vectorizer = CountVectorizer()

x_train = vectorizer.fit_transform(x_train)

model = LogisticRegression()

model.fit(x_train , y_train)

print(x_test)

x_test = vectorizer.transform(x_test)

prediction = model.predict(x_test)

for i in prediction:
    if i == 1:
        print("Spam")
    else:
        print("Not Spam")

