package Polynomial;

import Polynomial.View.MainWindow;
import javafx.application.Application;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        Secret.Secretaddition(5,3);
        Parent root = new MainWindow(primaryStage);
        primaryStage.setTitle("Polynomial Evaluator");
        primaryStage.getIcons().add(new Image("file:img/icon.jpg"));
        primaryStage.setScene(new Scene(root,600, 400));
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
