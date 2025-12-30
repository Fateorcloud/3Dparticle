import os
import urllib.request
import ssl

# 既然你有梯子，我们直接从官方源下载，保证文件完整
# 忽略 SSL 证书验证
ssl._create_default_https_context = ssl._create_unverified_context

# 创建 assets 文件夹
if not os.path.exists("assets"):
    os.makedirs("assets")

print("🚀 开始下载资源 (请保持梯子开启)...")

# 资源清单 (官方源)
base_url = "https://cdn.jsdelivr.net/npm"
files = {
    # Three.js
    "three.min.js": f"{base_url}/three@0.128.0/build/three.min.js",

    # MediaPipe 核心库
    "camera_utils.js": f"{base_url}/@mediapipe/camera_utils/camera_utils.js",
    "control_utils.js": f"{base_url}/@mediapipe/control_utils/control_utils.js",
    "drawing_utils.js": f"{base_url}/@mediapipe/drawing_utils/drawing_utils.js",
    "hands.js": f"{base_url}/@mediapipe/hands/hands.js",

    # MediaPipe 模型文件 (最关键的二进制文件)
    "hands_solution_packed_assets_loader.js": f"{base_url}/@mediapipe/hands/hands_solution_packed_assets_loader.js",
    "hands_solution_simd_wasm_bin.js": f"{base_url}/@mediapipe/hands/hands_solution_simd_wasm_bin.js",
    "hands_solution_simd_wasm_bin.wasm": f"{base_url}/@mediapipe/hands/hands_solution_simd_wasm_bin.wasm",
    "hand_landmark_full.tflite": f"{base_url}/@mediapipe/hands/hand_landmark_full.tflite"
}

for name, url in files.items():
    print(f"⬇️ 正在下载: {name} ...")
    try:
        # 下载到 assets 文件夹
        urllib.request.urlretrieve(url, f"assets/{name}")
        print(f"✅ 成功")
    except Exception as e:
        print(f"❌ 失败: {name} - {e}")

print("\n🎉 下载完成！现在你的 assets 文件夹里应该有 9 个文件。")