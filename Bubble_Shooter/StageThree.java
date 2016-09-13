import java.awt.*;
import java.awt.event.*; 
import javax.swing.*; 
import java.util.*;

class StageThree implements World {
  int score;
  Circle bullet;
  Launcher launcher;
  ArrayList<Circle> circles;
  int yCount = 20;
  int yCountTwo = 55;
  int yCountThree = 90;
  public void paintComponent(Graphics g) {
    for (Circle c : this.circles)
      c.draw(g); 
  }
  Color[] colors = new Color[] {Color.GREEN, Color.RED};
  Color c = pickcolor();
  private static int getRandomNumberInRange(int min, int max) {
    Random r = new Random();
    return r.nextInt((max - min) + 1) + min;
  }
  public Color pickcolor() {
    return colors[getRandomNumberInRange(0, 1)];
  }
  public StageThree() {
    this.bullet = new Circle(new Point(200, 400), this);
    this.launcher = new Launcher();
    this.circles = new ArrayList<Circle>();
    for (int i = 20; i < 400; i+=40) {
      this.circles.add(new Circle(new Point(i, yCount), this));
    }
    for (int z = 40; z < 380; z+=40) {
      this.circles.add(new Circle(new Point(z, yCountTwo), this));
    }
    for (int i = 20; i < 400; i+=40) {
      this.circles.add(new Circle(new Point(i, yCountThree), this));  
    }                     
  }
  public void draw(Graphics g) { 
    for (Circle c : this.circles)
      c.draw(g);
    this.launcher.draw(g);
    this.bullet.draw(g);
  } 
  public void update() { 
    this.bullet.move();
  }
  public boolean hasEnded() { 
    if (this.score == -1) {
      return true; 
    } else {
      return false; 
    }
  } 
  public void keyPressed(KeyEvent e) { 
    int keyCode = e.getKeyCode();
    if (keyCode == 37) {
      this.launcher.turnLeft();
    }
    else if (keyCode == 39) {
      this.launcher.turnRight();
    }
    else if (keyCode == 38) {
      this.launcher.launch(this.bullet);
    }
  }
  public static void main(String[] args) {
    BigBang game = new BigBang(30, new StageThree()); 
    JFrame frame = new JFrame("Bubble Shooter!"); 
    frame.getContentPane().add( game ); 
    frame.addKeyListener( game ); 
    frame.setVisible(true); 
    frame.setSize(410, 460); 
    Color myColor = new Color(136, 216, 242);
    frame.getContentPane().setBackground(myColor);
    frame.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE ); 
    game.start(); 
  }
}