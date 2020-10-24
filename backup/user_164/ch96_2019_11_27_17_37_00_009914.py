{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pygame'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-cd9bf15fefae>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mpygame\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mCIANO\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m255\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m255\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mBLACK\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mLARG\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m300\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'pygame'"
     ]
    }
   ],
   "source": [
    "import pygame\n",
    "\n",
    "CIANO = (0, 255, 255)\n",
    "BLACK = (0, 0, 0)\n",
    "LARG = 300\n",
    "\n",
    "class Quadrado(pygame.sprite.Sprite):\n",
    "    def __init__(self):\n",
    "        super(Quadrado, self).__init__()\n",
    "        self.image = pygame.Surface((10, 10))\n",
    "        self.image.fill(CIANO)\n",
    "        self.rect = self.image.get_rect()\n",
    "        self.rect.center = (LARG/2, LARG/2)\n",
    "\n",
    "pygame.init()\n",
    "screen = pygame.display.set_mode([LARG,LARG])\n",
    "clock = pygame.time.Clock()\n",
    "all_sprites = pygame.sprite.Group()\n",
    "all_sprites.add(Quadrado())\n",
    "\n",
    "while True:\n",
    "    clock.tick(60)\n",
    "    eventos = pygame.event.get()\n",
    "    all_sprites.update()\n",
    "    screen.fill(BLACK)\n",
    "    all_sprites.draw(screen)\n",
    "    pygame.display.flip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
