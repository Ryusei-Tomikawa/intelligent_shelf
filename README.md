# Intelligent_shelf
大原研究室にある電動陳列棚(Intelligent_shelf)をGazebo上で動作させるためのリポジトリ

### 動作方法
おそらくこのlaunchを起動することでGazebo,Rvizを起動できるはず
 ```shell
    $ roslaunch intelligent_shelf intelligent_shelf.launch
 ```

以下のスクリプトを起動することで動作することが可能
 ```shell
    $ rosrun intelligent_shelf move_shelf.py
 ```
 
 ### 問題点
 Gazebo上の棚を見ればわかるが棚が浮いているし、斜めることもある
 
 この原因はおそらく棚と棚板の重量とか慣性モーメントの値がおかしいと思われる
 
 Fusion360で出力したがなんかおかしいので、そこをなんとかすればいろいろ用途があるような気がする
 
 intelligent_shelf.stlがこのリポジトリにはいってないから棚が出力しない
 →確かモデルファイルが容量やばくてやめた気がする
