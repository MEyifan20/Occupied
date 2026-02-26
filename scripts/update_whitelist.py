import os
import re
import datetime

def process_whitelist(file_path):
    if not os.path.exists(file_path):
        print(f"⚠️ 找不到文件: {file_path}")
        return None, None

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    seen_rules = set()
    removed_count = 0

    for line in lines:
        stripped = line.strip()
        
        # 1. 保留空行、注释和头部元数据
        if not stripped or stripped.startswith('!') or stripped.startswith('['):
            new_lines.append(line)
            continue
        
        # 2. 内部智能去重：如果你不小心写了两遍同样的放行规则，自动清理多余的
        if stripped in seen_rules:
            removed_count += 1
            print(f"🗑️ 发现并清理重复规则: {stripped}")
            continue
        else:
            seen_rules.add(stripped)
            new_lines.append(line)

    # 生成最新的北京时间与版本号
    tz = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz)
    version_str = now.strftime("%Y.%m.%d.%H")
    time_str = now.strftime("%Y-%m-%d %H:%M")

    final_content = "".join(new_lines)
    
    # 替换文件头的版本和时间
    final_content = re.sub(r'! Version: .*', f'! Version: {version_str}', final_content)
    final_content = re.sub(r'! Updated: .*', f'! Updated: {time_str}', final_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"✅ 白名单处理完成，共清理 {removed_count} 条你的手误重复项。")
    print(f"✅ 白名单版本已更新至: {version_str}")
    return version_str, time_str

def update_readme(file_path, version_str, time_str):
    if not os.path.exists(file_path):
        print(f"⚠️ 找不到文件: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # 同步替换 README 中的版本和时间
    readme_content = re.sub(r'! Version: .*', f'! Version: {version_str}', readme_content)
    readme_content = re.sub(r'! Updated: .*', f'! Updated: {time_str}', readme_content)
    readme_content = re.sub(r'\*\*最后修改时间\*\*：.*', f'**最后修改时间**：{time_str} (GMT+8)', readme_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(f"✅ README.md 同步更新完毕。")

if __name__ == '__main__':
    print("🚀 开始执行白名单自动维护任务...")
    
    # 执行白名单文件处理
    v_str, t_str = process_whitelist('iOS-OmniGuard-Whitelist.txt')
    
    # 如果白名单处理成功，同步更新 README
    if v_str and t_str:
        update_readme('README.md', v_str, t_str)
        
    print("🎉 全部任务执行完毕，仓库已成功保活！")

