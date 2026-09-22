from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    player_choice = int(data.get('choice'))
    player_name = data.get('name')
    
    # Validate input
    if player_choice not in [1, 2, 3]:
        return jsonify({'error': 'Invalid choice. Please select 1, 2, or 3.'}), 400
    
    # Computer makes a choice
    computer_choice = random.randint(1, 3)
    
    # Convert choices to text
    choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
    player_choice_text = choices[player_choice]
    computer_choice_text = choices[computer_choice]
    
    # Determine the winner
    if computer_choice == player_choice:
        result = "It's a Tie! Both of you are equally awesome!"
    elif ((player_choice == 1 and computer_choice == 3) or 
          (player_choice == 2 and computer_choice == 1) or 
          (player_choice == 3 and computer_choice == 2)):
        result = f"Congratulations {player_name}! You are the WINNER!"
    else:
        result = f"The Computer WON! Better luck next time, {player_name}!"
    
    return jsonify({
        'player_choice': player_choice_text,
        'computer_choice': computer_choice_text,
        'result': result
    })

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
