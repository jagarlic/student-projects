import java.awt.*;
import java.util.*;

public class Circle {
  boolean safe = false;
  int radius = 20;
  double vx, vy;
  int neighbors;
  Point center;
  StageThree world;
  Color[] colors = new Color[] {Color.GREEN, Color.RED};
  Color c = pickcolor();
  private static int getRandomNumberInRange(int min, int max) {
    Random r = new Random();
    return r.nextInt((max - min) + 1) + min;
  }
  public Color pickcolor() {
    return colors[getRandomNumberInRange(0, 1)];
  }
  public String toString() {
    return "(" + neighbors + ")";
  }
  public Circle(Point center, StageThree world) {
    this.center = center;
    this.world = world;
  }
  public void draw(Graphics g) {
    g.setColor(this.c);
    g.fillOval( (center.x - 20), (center.y - 20), 40, 40);
    g.setColor(Color.BLACK);
    g.drawOval( (center.x - 20), (center.y - 20), 40, 40);
    g.drawString("" + this.neighbors, center.x, center.y );
    g.drawString("Your score is: " + this.world.score, 40, 370);
  }
  public void move() {
    this.neighbors(this.world.circles);
    this.center.x += this.vx;
    this.center.y += this.vy;
    if (this.center.y < 21) {
      this.vx = 0;
      this.vy = 0;
      this.world.circles.add(this);
      this.world.bullet = new Circle(new Point(200, 400), this.world);
    } else if (this.center.x < 21 || this.center.x > 370) {
      this.vx *= -1;
    } else {
      boolean stuck = false;
      for (Circle c : this.world.circles) {
        if (this.overlaps(c)) {
          stuck = true;
        }
      }
      if (stuck) {
        this.vx = 0;
        this.vy = 0;
        this.world.circles.add(this);
        this.world.bullet = new Circle(new Point(200, 400), this.world);
        this.neighbors(this.world.circles);
        this.purge(this.world.circles);
        if (this.center.y + 40 >= 400) {
          this.world.score = -1;
        }
      }
    }
  }
  public boolean overlaps(Circle other) {
    return this.radius + other.radius + 2 >= this.center.distanceTo(other.center);
  }
  public void neighbors(ArrayList<Circle> circles) {
    for (Circle c : this.world.circles)
      if (c != this && c.overlaps(this) && (c.c == this.c)) {
      this.neighbors += 1;
      c.neighbors += 1;
    }
  }
  public void purge(ArrayList<Circle> circles) {
    for (Circle x : this.world.circles)
      x.safe = true;
    ArrayList<Circle> result = new ArrayList<Circle>();
    for (Circle c : this.world.circles) {
      for (Circle c1 : this.world.circles) {
        if (c.overlaps(c1)) {
          if (c1.neighbors >= 3 && (c.c == c1.c)) {
            for (Circle c2 : this.world.circles) {
              if ((c1.overlaps(c2) || c.overlaps(c2)) && (c1.c == c2.c) && (c.c == c2.c))  {
                if (c2.safe != false) {
                  c2.safe = false;
                  this.world.score += 1;
                }
                if (c.safe != false) {
                  c.safe = false;
                  this.world.score += 1;
                }
                if (c1.safe != false) {
                  c1.safe = false;
                  this.world.score += 1;
                }
              }
            }
          } else {}
        }
      }
    }
    for (Circle c2 : this.world.circles) {
      if (c2.safe) {
        result.add(c2);
      }
    }
    this.world.circles = result;
  }
}

