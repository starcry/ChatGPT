def parse_file(file_path):
    with open(file_path, 'r') as file:
        paragraphs = file.read().split('\n\n')

        if len(paragraphs) != 2:
            return "The file should contain exactly two paragraphs. The first one describing the food intake and the second one describing the physical activities."

        food_description, activity_description = paragraphs

        message = f"""
        Hello ChatGPT,

        Today, I consumed the following:
        {food_description}

        I would like to know the calorie content for each item consumed.

        My physical activities included the following:
        {activity_description}

        I would like to know the calories burned for each physical activity mentioned.

        Based on this information, could you please calculate:
        1. My daily weight gain or loss.
        2. My daily calorie gain or loss.

        Thank you!
        """

        return message

# Usage
file_path = 'intake_output'  # Replace with the actual path to your text file
message = parse_file(file_path)
print(message)

