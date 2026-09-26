# 安装指南 Install

## 方式一:Color Presets(推荐,支持昼夜自动切换)

1. 双击 `Morandi-Day.itermcolors` 和 `Morandi-Night.itermcolors`,iTerm 会把它们导入为 Color Preset;
   也可以手动导入:`iTerm2 → Settings (⌘,) → Profiles → Colors → Color Presets… → Import…` 选择文件。
2. 在同一个 Colors 标签页里,`Color Presets…` 选择 `Morandi-Day` 或 `Morandi-Night`,即应用到当前 Profile。

## 方式二:动态 Profile(固定配色,一键启用)

```bash
cp dynamic-profiles/*.json ~/Library/Application\ Support/iTerm2/DynamicProfiles/
```

iTerm 会自动加载,无需重启:菜单栏 `Profiles` → 选「莫兰迪·昼」或「莫兰迪·夜」即可用该配色开新窗口;
`Settings → Profiles → 选中 → Other Actions… → Set as Default` 可设为默认 Profile。

> 注意:动态 Profile 是固定配色,不参与昼夜自动切换;需要自动切换请用方式一。

## 昼夜自动切换(随 macOS 系统)

要求 iTerm2 ≥ 3.5。

1. 先用**方式一**把两个配色导入为 Color Preset;
2. `Settings → Profiles` 选中你的 Profile → `Colors` 标签;
3. 勾选 **Use separate colors for light and dark mode**;
4. 标签页会出现 **Editing** 切换控件:
   切到 `Light` → `Color Presets…` 选 **Morandi-Day**;
   切到 `Dark` → `Color Presets…` 选 **Morandi-Night**;
5. macOS `系统设置 → 外观` 设为**自动**(或手动切换深色模式),iTerm 配色会即时跟随系统切换。

参考:[iTerm2 官方文档 - Colors](https://iterm2.com/documentation-preferences-profiles-colors.html)

## Kimi Code CLI 界面主题

仓库附带同色系的 Kimi Code CLI 主题(`kimi-code/morandi-day.json` / `morandi-night.json`):

```bash
cp kimi-code/*.json ~/.kimi-code/themes/
```

启用方式(二选一):

- 在 CLI 会话中运行 `/theme`,选择 `Custom: morandi-day` 或 `Custom: morandi-night`;
- 或编辑 `~/.kimi-code/tui.toml`:`theme = "morandi-night"`,然后在会话里运行 `/reload-tui` 生效。

> CLI 主题在会话启动时确定,无法跟随系统自动切换;系统外观变化后请用 `/theme` 手动切换配套版本。

## 演示

```bash
scripts/color-demo        # 查看昼主题演示
scripts/color-demo night  # 查看夜主题演示
```

## 卸载

- Color Presets:`Color Presets…` 菜单中选中对应项删除;
- 动态 Profile:删除 `~/Library/Application Support/iTerm2/DynamicProfiles/Morandi-*.json`;
- CLI 主题:删除 `~/.kimi-code/themes/morandi-*.json`,并把 `tui.toml` 的 `theme` 改回 `auto`。
