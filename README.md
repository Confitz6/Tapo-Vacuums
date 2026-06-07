# Tapo Vacuum Advanced
A custom Home Assistant HACS integration giving you full control, editing, and 2026 area mapping for TP-Link Tapo robot vacuums.

# 🧹 Tapo Vacuum Advanced
**An Advanced Control & Feature Unlocker for Tapo Robot Vacuums in Home Assistant**

This dedicated integration provides granular control, setting customization, and advanced mapping capabilities for your Tapo robot vacuum. It fully leverages the **March 2026.3 Area Mapping ("A clean sweep")** update, allowing you to map your Tapo room segments directly to Home Assistant Areas for seamless UI targeting.

## 🚀 Features
* **Full Control:** Advanced states (Start, Pause, Dock, Stop) interacting directly with Tapo local/polling protocols.
* **2026.3 Area Mapping:** Send your vacuum to specific rooms using native Home Assistant Areas and the `vacuum.clean_area` action.
* **Granular Editing:** Exposes secondary entities for real-time adjustments like mopping water flow levels and fan speed presets.

## 🤖 Target Hardware
* Optimized for **TP-Link Tapo Robot Vacuums** (including LiDAR mapping models like the RV series).

## 🛠️ Installation
1. Copy your GitHub repository URL.
2. In Home Assistant, go to **HACS** > **Integrations**.
3. Click the three dots in the top-right corner and select **Custom repositories**.
4. Paste the URL, select **Integration** as the Category, and click **Add**.
5. Download and restart Home Assistant.
6. Go to **Settings** > **Devices & Services** > **Add Integration** and search for **Tapo Vacuum Advanced**.
