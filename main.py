from turtle import Screen, Turtle
from snake import Snake
from scroreboard import Score_board
from food import Food
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
score_board = Score_board()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up,"Up") 
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        score_board.increase_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score_board.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score_board.game_over()




screen.exitonclick()    
