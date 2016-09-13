import java.awt.*;

public class Launcher {
  int angle = 90; 
  int angle2 = 90;
  public void draw(Graphics g) {
    g.drawOval(200 - 60, 400 - 60, 120, 120);
    int x = (int) (200 + Math.cos(Math.PI * angle / 180) * 60);
    int y = (int) (400 - Math.sin(Math.PI * angle / 180) * 60);
    int y2 = (int) (400 - Math.sin(Math.PI * angle / 180) * 380);
    int x2 = (int) (200 + Math.cos(Math.PI * angle / 180) * 380);
    int y3 = (int) (y2 - Math.sin(Math.PI * angle2 / 180) * 550);
    int x3 = (int) (x2 + Math.cos(Math.PI * angle2 / 180) * 550);
    if (x2 >= 370) {
      x2 = 370;
      g.drawLine(370, y2, x3, y3);
    }
    if (x2 <= 20) {
      x2 = 20;
      g.drawLine(20, y2, x3, y3);
    }
    g.fillOval(x2 - 5, y2 - 5, 10, 10);
    g.fillOval(x3 - 5, y3 - 5, 10, 10);
    g.drawLine(200, 400, x2, y2);;
    
  }
  public void turnLeft() {
    this.angle += 2;
    this.angle2 -= 2;
    
  }
  public void turnRight() {
    this.angle -= 2;
    this.angle2 += 2;
  } 
  public void launch(Circle bullet) {
    bullet.vx = 5 * Math.cos( Math.PI * this.angle / 180 );
    bullet.vy = -5 * Math.sin( Math.PI * this.angle / 180 );
  }
}
