# ASMK_yoda
## Training : @Jupyterlab
#### 実行用ノートブック：Jupyterlab_exe.ipynb
 ※ASMK_yoda/howの中身は変更済み
 （変更点はコメントアウト記載）
 ※ディレクトリ構成に応じてディレクトリ名を変更
#### /how/stages/train_Jupyter.pyを/how/stages/train.pyに変更して実行
  → 学習開始 → 5エポックごとに中断(/how/how_temp/temp.pthにパラメータが保存)
  → temp.pthから学習パラメータを読み込んで再開

## Evaluating : @Google Colab
#### ~~実行用ノートブック：Githubから実行5.0.ipynb
#### Jupyterで学習した/how/how_temp/temp.pthをコピー
 ※5、10、15、20エポックまで学習済みのtemp.pthを使用
#### /how/stages/train_Colab.pyを/how/stages/train.pyに変更して実行
  → 5、10、15、20エポックまでの学習結果を用いて評価開始~~

#### 実行用ノートブック：Githubから実行5.1.ipynb
#### Jupyterで学習した/how/how_temp/temp.pthをGoogle driveからマウント
 ※5、10、15、20エポックまで学習済みのtemp.pthを使用
#### "# 修正済みプログラムのclone"のセル実行
#### "# temp.pthファイルをgoogle driveからコピー"のセル実行
#### "# 元コードおよびデータ clone"のセル実行
  → /how/how_data/train/mitsubishi_datasetに/local/mitsubishi_datasetの./png_imagesを移動
#### "# asmk"のセル実行
  → faissのインストール
#### /how/stages/train_Colab.pyを/how/stages/train.pyに変更
#### "# コードの実行"のセル実行
  → 5、10、15、20エポックまでの学習結果を用いて評価開始
