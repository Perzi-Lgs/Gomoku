##
## EPITECH PROJECT, 2019
## makefile
## File description:
## project: gomoku
##

CC		=	cp

CLEAN		=	echo clean

NAME		=	pbrain-gomoku-ai

RM		=	rm -rf

SRC		=	main.py

all:	$(NAME)

$(NAME):	$(SRC)
		$(CC) $(SRC) $(NAME)

clean:
	$(CLEAN)

fclean:	clean
	$(RM) $(NAME) *~
	$(RM) __pycache__

re:	fclean all
