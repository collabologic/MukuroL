#!/usr/bin/env python3
import os
import shutil
import argparse
import yaml
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .core.mukurol import MukuroL  # MukuroLクラスのインポート
from bs4 import BeautifulSoup
import threading
import traceback

# デフォルト設定
DEFAULT_SRC_DIR = "src"
DEFAULT_DIST_DIR = "dist"
DEFAULT_CONFIG_FILE = "mkl.config.yml"
DEFAULT_PORT = 6961

class MKLFileHandler(FileSystemEventHandler):
    def __init__(self, src_dir, dist_dir, mukurol):
        self.src_dir = src_dir
        self.dist_dir = dist_dir
        self.mukurol = mukurol

    def on_modified(self, event):
        if event.event_type == 'modified' and event.src_path.endswith(".mkl"):
            print(f"File {event.src_path} has been modified. Generating HTML...")
            self.generate_html(event.src_path)
            print("HTML generated. Refresh your browser.")

    def generate_html(self, src_file):
        # ファイル名から出力ファイル名を決定
        base_name = src_file.replace("src/", "").replace(".mkl", ".html")
        dist_file = os.path.join(self.dist_dir, base_name)
        os.makedirs(os.path.dirname(dist_file), exist_ok=True)
        print(f"Generating HTML from {src_file} to {dist_file}")
       
        try:
            with open(src_file, "r") as f:
                mukurol_text = f.read()
            layout_html = self.mukurol.generate_html(mukurol_text)
            # レイアウトHTMLをファイルに出力
            if layout_html != "":
                with open(dist_file, "w") as f:
                    f.write(str(layout_html))
        except Exception as e:
            print(f"Error generating HTML for {src_file}: {e}")
            traceback.print_exc()

def get_all_files(directory):
    """
    指定されたディレクトリ内のすべてのファイル（サブディレクトリを含む）を取得します。
    """
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

def init_command(path):
    """
    指定のディレクトリに、src, distディレクトリと、空のmkl.config.ymlを作成します。
    """
    src_path = os.path.join(path, DEFAULT_SRC_DIR)
    dist_path = os.path.join(path, DEFAULT_DIST_DIR)
    config_path = os.path.join(path, DEFAULT_CONFIG_FILE)

    os.makedirs(src_path, exist_ok=True)
    os.makedirs(dist_path, exist_ok=True)

    # style.cssをdistディレクトリにコピー
    src_css = os.path.join(os.path.dirname(__file__), "style.css")
    dist_css = os.path.join(dist_path, "style.css")
    if os.path.exists(src_css):
        shutil.copy(src_css, dist_css)
        print(f"  - Copied style.css to: {dist_css}")
    else:
        print(f"  - style.css not found at: {src_css}")

    with open(config_path, "w") as f:
        yaml.dump({}, f)  # 空のYAMLファイルを作成

    print(f"Initialized MukuroL project in {path}")
    print(f"  - Created directory: {src_path}")
    print(f"  - Created directory: {dist_path}")
    print(f"  - Created file: {config_path}")

def generate_html_file(src_file, output_file, mukurol):
    """
    指定のソースファイルからHTMLファイルを生成します。
    """
    try:
        # 出力先のディレクトリが存在しない場合は作成
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        print(f"Generating HTML from {src_file} to {output_file}")

        with open(src_file, "r") as f:
            mukurol_text = f.read()
        layout_html = mukurol.generate_html(mukurol_text)
        if layout_html != "":
            with open(output_file, "w") as f:
                f.write(str(layout_html))
        print(f"Generated HTML from {src_file} to {output_file}")
    except Exception as e:
        print(f"Error generating HTML for {src_file}: {e}")
        traceback.print_exc()

def generate_command(input_file=None, output_file=None):
    """
    指定のソースファイルから、出力先ファイルにHTMLファイルを作成します。
    未指定の場合は、srcディレクトリのファイル全てからdistディレクトリに結果を吐き出します。
    """
    mukurol = MukuroL()  # MukuroLクラスのインスタンスを作成

    if input_file:
        # 単一ファイルの処理
        src_file = input_file
        if not output_file:
            # 出力ファイル名が未指定の場合は、デフォルトのdistディレクトリに出力
            base_name = os.path.basename(src_file).replace(".mkl", ".html")
            output_file = os.path.join(DEFAULT_DIST_DIR, base_name)

        process_single_file(src_file, output_file, mukurol)

    else:
        # srcディレクトリのファイルを全て処理
        process_all_files(DEFAULT_SRC_DIR, DEFAULT_DIST_DIR, mukurol)

def process_single_file(src_file, output_file, mukurol):
    """
    単一のMKLファイルを処理してHTMLを生成します。
    """
    generate_html_file(src_file, output_file, mukurol)

def process_all_files(src_dir, dist_dir, mukurol):
    """
    srcディレクトリ以下のすべてのMKLファイルを処理してHTMLを生成します。
    """
    if not os.path.exists(src_dir):
        print(f"Error: Source directory '{src_dir}' not found.")
        return

    mkl_files = [f.replace("src/", '') for f in get_all_files(src_dir) if f.endswith(".mkl")]

    for filename in mkl_files:
        src_file = os.path.join(src_dir, filename)
        base_name = filename.replace(".mkl", ".html")
        dist_file = os.path.join(dist_dir, base_name)
        os.makedirs(os.path.dirname(dist_file), exist_ok=True)

        process_single_file(src_file, dist_file, mukurol)

def watch_command():
    """
    src内のmklファイルを監視し、更新があった場合は、そのmklファイルからHTMLを生成します。
    """
    src_dir = DEFAULT_SRC_DIR
    dist_dir = DEFAULT_DIST_DIR

    if not os.path.exists(src_dir):
        print(f"Error: Source directory '{src_dir}' not found.")
        return

    os.makedirs(dist_dir, exist_ok=True)

    mukurol = MukuroL()  # MukuroLクラスのインスタンスを作成

    # 初期HTMLファイルを生成
    mkl_files = [f.replace("src/",'') for f in get_all_files(src_dir) if f.endswith(".mkl")]
    for filename in mkl_files:
        print(f"Generating initial HTML from {filename}!!!")
        if filename.endswith(".mkl"):
            src_file = os.path.join(src_dir, filename)
            MKLFileHandler(src_dir, dist_dir, mukurol).generate_html(src_file)

    print("Starting file watcher...")
    # ファイル監視の設定
    event_handler = MKLFileHandler(src_dir, dist_dir, mukurol)
    observer = Observer()
    observer.schedule(event_handler, src_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def main():
    parser = argparse.ArgumentParser(description="MukuroL CLI tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init コマンド
    init_parser = subparsers.add_parser("init", help="Initialize a new MukuroL project")
    init_parser.add_argument("path", help="Path to the project directory")

    # generate コマンド
    generate_parser = subparsers.add_parser("generate", help="Generate HTML from MKL files")
    generate_parser.add_argument("-i", "--input", dest="input_file", help="Path to the input MKL file")
    generate_parser.add_argument("-o", "--output", dest="output_file", help="Path to the output HTML file")

    # watch コマンド
    subparsers.add_parser("watch", help="Watch for changes in the source directory and automatically regenerate HTML")

    args = parser.parse_args()

    if args.command == "init":
        init_command(args.path)
    elif args.command == "generate":
        generate_command(args.input_file, args.output_file)
    elif args.command == "watch":
        watch_command()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()