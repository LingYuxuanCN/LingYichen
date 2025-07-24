import webbrowser
import subprocess
import sys

def get_pypi_url(package_name):
    """生成PyPI包的URL"""
    # 标准化包名（PyPI包名不区分大小写，但URL通常用小写）
    normalized_name = package_name.lower()
    return f"https://pypi.org/project/{normalized_name}/"


def main():
    print("PyPI包URL查询工具")
    print("输入'q'退出程序\n")

    while True:
        package_name = input("请输入要查询的包名: ").strip()

        if package_name.lower() == 'q':
            print("程序已退出")
            break

        if not package_name:
            print("包名不能为空，请重新输入\n")
            continue

        # 生成URL
        url = get_pypi_url(package_name)
        print(f"\n对应的PyPI地址: {url}")

        # 自动用Edge浏览器打开网页
        try:
            if sys.platform.startswith('win32'):
                # Windows系统通过命令调用Edge
                subprocess.run(['start', 'msedge', url], shell=True, check=True)
                print("已自动用Edge浏览器打开链接\n")
        except:
            # 打开失败时保留原有的询问逻辑
            print("自动打开失败，")
            open_choice = input("是否要在浏览器中打开? (y/n): ").strip().lower()
            if open_choice == 'y':
                webbrowser.open(url)
                print("已在浏览器中打开链接\n")
            else:
                print("可手动复制上面的URL访问\n")


if __name__ == "__main__":
    main()