import turtle, random

border = turtle.Turtle()# черепашка
border.hideturtle() # спрятать черепашку
border.speed(0)     # скорость отрисовки
border.pensize(5)
border.up()        
border.goto(-250, 250)
border.down()
border.goto(-250, -250)
border.goto(250, -250)
border.goto(250, 250)
# создание доски почтиквадрат

window = turtle.Screen()
window.bgcolor('yellow')# цвет окна
window.tracer(40) # tracter функция фпс типа

balls = []
count = 50
forms = ['circle', 'square', 'triangle', 'turtle']
# меняет формы черепашек

for i in range(count): 
    ball = turtle.Turtle(shape= random.choice(forms))
    red = random.random()
    green = random.random()
    blue = random.random()
    ball.color(red, green, blue)
    ball.up()
    ball.goto(random.randint(-200, 200), random.randint(100,300)) # мячик появиться выше серидины
    ball.speedY = 0
    ball.speedx = random.randint(-3, 3) # в какую сторону полетит мячик вначале игры
    ball.angle = random.randint(-5, 5) # переменная УГОЛ
    balls.append(ball)
    # цикл создает 10 мячиков

gravitation = 0.05
 
while True:
    window.update()
    for ball in balls:
        ball.left(ball.angle) 
        ball.speedY = ball.speedY - gravitation
        ball.goto(ball.xcor() + ball.speedx, ball.ycor() + ball.speedY)

        if ball.ycor() <=-250:
            ball.sety(-250)
            ball.speedY = -ball.speedY
            
        if ball.xcor() >= 250 or ball.xcor() <= -250:
            ball.speedx = -ball.speedx
    # Если у мячика текущая координата по y будет <= 250
    # тогда скорость мячика изменить на провотивоположн
    # короче делает так что бы мячик прыгал
window.mainloop()
