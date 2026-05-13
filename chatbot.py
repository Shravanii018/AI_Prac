print("===================================")
print("     CUSTOMER SUPPORT CHATBOT")
print("===================================")

name = input("Enter your name: ")

print(f"\nHello {name}!")
print("I am Customer Support Bot.")
print("Type 'bye' to exit.\n")

# ---------- MENU ----------
print("========== MENU ==========")
print("1. hello / hi       -> Greetings")
print("2. order / track    -> Track Order")
print("3. refund           -> Refund Status")
print("4. delivery         -> Delivery Details")
print("5. payment          -> Payment Methods")
print("6. product          -> Product Information")
print("7. support / help   -> Customer Support")
print("8. complaint        -> Register Complaint")
print("9. thank you        -> Thanking Bot")
print("10. bye             -> Exit Chat")
print("==========================\n")

while True:

    user = input("You: ").lower()

    # Greetings
    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you today?")

    # Order Status
    elif "order" in user or "track" in user:
        print("Bot: Your order is currently being processed.")

    # Refund
    elif "refund" in user:
        print("Bot: Refund will be processed within 5-7 working days.")

    # Delivery
    elif "delivery" in user:
        print("Bot: Your delivery is expected within 3 days.")

    # Payment
    elif "payment" in user:
        print("Bot: Payment can be made using UPI, Card, or Net Banking.")

    # Product Information
    elif "product" in user:
        print("Bot: Please visit our website for detailed product information.")

    # Contact Support
    elif "support" in user or "help" in user:
        print("Bot: Customer care number is 9876543210.")

    # Complaint
    elif "complaint" in user:
        print("Bot: Your complaint has been registered successfully.")

    # Thanks
    elif "thank" in user:
        print("Bot: You're welcome!")

    # Exit
    elif "bye" in user:
        print("Bot: Thank you for contacting customer support.")
        print("Bot: Have a nice day!")
        break

    # Unknown Input
    else:
        print("Bot: Sorry, I could not understand your query.")