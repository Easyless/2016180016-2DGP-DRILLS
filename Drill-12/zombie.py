import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import main_state

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 15.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

animation_names = ['Attack', 'Dead', 'Idle', 'Walk']


class Zombie:
    images = None

    def load_images(self):
        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombiefiles/female/" + name + " (%d)" % i + ".png") for i in
                                       range(1, 11)]

    def __init__(self):
        self.target_x, self.target_y = None, None
        self.x = random.randint(50, 1280 - 50)
        self.y = random.randint(50, 1024 - 50)
        self.font = load_font('ENCR10B.TTF', 16)
        self.load_images()
        self.HP = 100
        self.dir = random.random() * 2 * math.pi  # random moving direction
        self.speed = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.frame = 0
        self.build_behavior_tree()

    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(200, self.y, 1024 - 50)

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random() * 2 * math.pi

        return BehaviorTree.SUCCESS
        pass

    def find_player(self):
        boy = main_state.get_boy()
        distance = (boy.x - self.x) ** 2 + (boy.y - self.y) ** 2
        if distance < (PIXEL_PER_METER * 8) ** 2:
            if self.HP > boy.HP:
                self.dir = math.atan2(boy.y - self.y, boy.x - self.x)
            else:
                self.dir = math.atan2(-(boy.y - self.y), -(boy.x - self.x))
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass

    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        return BehaviorTree.SUCCESS
        pass

    def find_balls(self):
        balls = main_state.get_balls()
        for ball in balls:
            distance = (ball.x - self.x) ** 2 + (ball.y - self.y) ** 2
            if distance < (PIXEL_PER_METER * 5) ** 2:
                self.dir = math.atan2(ball.y - self.y, ball.x - self.x)
                return BehaviorTree.SUCCESS
            else:
                self.speed = 0
                return BehaviorTree.FAIL
        pass

    def move_to_ball(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        return BehaviorTree.SUCCESS
        pass

    def build_behavior_tree(self):
        wander_node = LeafNode("Wander", self.wander)
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        find_ball_node = LeafNode("Find Ball", self.find_balls)
        move_to_ball_node = LeafNode("Move to Ball", self.move_to_ball)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node)
        chase_ball_node = SequenceNode("Chase ball")
        chase_ball_node.add_children(find_ball_node, move_to_ball_node)
        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_child(chase_node)
        wander_chase_node.add_child(chase_ball_node)
        wander_chase_node.add_child(wander_node)
        self.bt = BehaviorTree(wander_chase_node)
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.bt.run()
        pass

    def draw(self):
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)
        draw_rectangle(*self.get_bb())
        self.font.draw(self.x - 60, self.y + 50, '(HP: %3.2f)' % self.HP, (255, 255, 0))
    def handle_event(self, event):
        pass
