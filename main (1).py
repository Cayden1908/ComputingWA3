import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Question Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Define font
font = pygame.font.Font(None, 30)

# Define variables
score = 0
game_over = False
restart = False
lose = 0
win = 0

# Define question and answer options
questions = {
  "What is the capital of France?": {
        "options": ["Paris", "Berlin", "Rome", "Madrid"],
        "answer": "Paris"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    "Which country is home to the kangaroo?": {
        "options": ["Australia", "Argentina", "Canada", "Egypt"],
        "answer": "Australia"
    },
    "What is the largest ocean in the world?": {
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    "What is the capital of Japan?": {
        "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"],
        "answer": "Tokyo"
    },
    "Which European country is known as Holland?": {
        "options": ["Netherlands", "Sweden", "Belgium", "Austria"],
        "answer": "Netherlands"
    },
    "What is the currency of Brazil?": {
        "options": ["Real", "Peso", "Yen", "Rupee"],
        "answer": "Real"
    },
    "Which animal is known as the 'King of the Jungle'?": {
        "options": ["Lion", "Tiger", "Elephant", "Giraffe"],
        "answer": "Lion"
    },
    "What is the official language of China?": {
        "options": ["Mandarin", "Cantonese", "English", "Spanish"],
        "answer": "Mandarin"
    },
    "Which mountain range is the longest in the world?": {
        "options": ["Andes", "Himalayas", "Rocky Mountains", "Alps"],
        "answer": "Andes"
    },
    "What is the national flower of India?": {
        "options": ["Lotus", "Rose", "Tulip", "Sunflower"],
        "answer": "Lotus"
    },
    "Which country is known for its tulips?": {
        "options": ["Netherlands", "France", "Italy", "Germany"],
        "answer": "Netherlands"
    },
    "Which country is famous for the pyramids?": {
        "options": ["Egypt", "Greece", "Mexico", "China"],
        "answer": "Egypt"
    },
    "Which is the largest desert in the world?": {
        "options": ["Sahara Desert", "Gobi Desert", "Atacama Desert", "Antarctica"],
        "answer": "Sahara Desert"
    },
    "Which country is home to the Great Barrier Reef?": {
        "options": ["Australia", "Brazil", "Canada", "India"],
        "answer": "Australia"
    },
    "What is the tallest mountain in the world?": {
        "options": ["Mount Everest", "K2", "Kilimanjaro", "Mount Fuji"],
        "answer": "Mount Everest"
    },
    "What is the currency of Japan?": {
        "options": ["Yen", "Dollar", "Euro", "Pound"],
        "answer": "Yen"
    },
    "Which country is known as the 'Land of the Rising Sun'?": {
        "options": ["Japan", "China", "Korea", "Vietnam"],
        "answer": "Japan"
    },
    "What is the official language of Spain?": {
        "options": ["Spanish", "Portuguese", "French", "Italian"],
        "answer": "Spanish"
    },
    "Which animal is known for its black and white stripes?": {
        "options": ["Zebra", "Giraffe", "Elephant", "Panda"],
        "answer": "Zebra"
    }
    # ... (same questions and answers as before)
}

question = random.choice(list(questions.keys()))
asked_questions = []

# Define button class
class Button:
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, display, font):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))
        text_surface = font.render(self.text, True, black)
        text_x = self.x + (self.width - text_surface.get_width()) // 2
        text_y = self.y + (self.height - text_surface.get_height()) // 2
        display.blit(text_surface, (text_x, text_y))

# Define buttons
start_button = Button(white, display_width // 2 - 75, display_height // 2 + 50, 150, 50, "Start")
restart_button = Button(white, display_width // 2 - 75, display_height // 2 + 50, 150, 50, "Restart")

# Starting page loop
starting_page = True
while starting_page:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            starting_page = False

        if event.type == pygame.MOUSEBUTTONDOWN and start_button.x <= event.pos[0] <= start_button.x + start_button.width and start_button.y <= event.pos[1] <= start_button.y + start_button.height:
            starting_page = False

    display.fill(white)
    start_text = font.render("Press Start to Begin", True, black)
    display.blit(start_text, (display_width // 2 - start_text.get_width() // 2, display_height // 2 - start_text.get_height() // 2))

    # Draw start button
    start_button.draw(display, font)

    pygame.display.update()

while True: 
    while not game_over:
    # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_option = questions[question]["options"][0]
                elif event.key == pygame.K_2:
                    selected_option = questions[question]["options"][1]
                elif event.key == pygame.K_3:
                    selected_option = questions[question]["options"][2]
                elif event.key == pygame.K_4:
                    selected_option = questions[question]["options"][3]
                
                if selected_option == questions[question]["answer"]:
                    score += 1
                    win += 1
                    print("OMG you got it correct ")
                else:
                    score -= 1
                    lose += 1
                    print("BRUH why u sell the question, even Jovan could get it correct")
    
                asked_questions.append(question)
                
                if score >= 5:
                  
                  game_over = True
                else:
                    while question in asked_questions:
                        question = random.choice(list(questions.keys()))
                    random.shuffle(questions[question]["options"])
              
    
        # Display background and question
        display.fill(white)
        question_text = font.render(question, True, black)
        display.blit(question_text, (display_width // 2 - question_text.get_width() // 2, 50))
    
        # Display answer options
        option_y = 100
        for i, option in enumerate(questions[question]["options"]):
            option_text = font.render(f"{i+1}. {option}", True, black)
            display.blit(option_text, (display_width // 2 - option_text.get_width() // 2, option_y))
            option_y += 50
    
        # Highlight correct answer if user gets it wrong
        if game_over and selected_option != questions[question]["answer"]:
            correct_option_index = questions[question]["options"].index(questions[question]["answer"])
            correct_option_text = font.render(f"{correct_option_index+1}. {questions[question]['answer']}", True, green)
            display.blit(correct_option_text, (display_width // 2 - correct_option_text.get_width() // 2, 100 + correct_option_index * 50))
    
        # Display score
        score_text = font.render("Score: " + str(score), True, black)
        display.blit(score_text, (10, 10))
    
        pygame.display.update()

        if restart:
            restart = False
            game_over = False

# Ending page loop
    while game_over == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
        k = pygame.key.get_pressed()
        if k[pygame.K_r]: 
           
            score = 0
            question = random.choice(list(questions.keys()))
            asked_questions.clear()
            game_over = False
        
        display.fill(white)
        ending_text = font.render("Game Over! Final Score: " + str(score), True, black)
        display.blit(ending_text, (display_width // 2 - ending_text.get_width() // 2, 250))
    
        restart_text = font.render("Press 'R' to Restart", True, black)
        display.blit(restart_text, (display_width // 2 - restart_text.get_width() // 2, 310))

        win_text = font.render("Points gained: " + str(win), True, black)
        display.blit(win_text, (display_width // 2 - restart_text.get_width() // 2, 270))

        lose_text = font.render("Points lost: " + str(lose), True, black)
        display.blit(lose_text, (display_width // 2 - restart_text.get_width() // 2, 290))
    
        pygame.display.update()
    
        # Draw restart button
        #restart_button.draw(display, font)
    
        pygame.display.update()
