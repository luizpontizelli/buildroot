import infra.basetest


class TestATFVexpress(infra.basetest.BRTest):
    config = \
        """
        BR2_aarch64=y
        BR2_TOOLCHAIN_EXTERNAL=y
        BR2_TOOLCHAIN_EXTERNAL_LINARO_AARCH64=y
        BR2_TARGET_ARM_TRUSTED_FIRMWARE=y
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_CUSTOM_GIT=y
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_CUSTOM_REPO_URL="https://github.com/ARM-software/arm-trusted-firmware.git"
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_CUSTOM_REPO_VERSION="v2.5"
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_PLATFORM="juno"
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_FIP=y
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_UBOOT_AS_BL33=y
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_NEEDS_DTC=y
        BR2_TARGET_UBOOT=y
        BR2_TARGET_UBOOT_BOARDNAME="vexpress_aemv8a_juno"
        BR2_TARGET_UBOOT_CUSTOM_VERSION=y
        BR2_TARGET_UBOOT_CUSTOM_VERSION_VALUE="2020.07"
        BR2_TARGET_VEXPRESS_FIRMWARE=y
        """

    def test_run(self):
        pass


class TestATFAllwinner(infra.basetest.BRTest):
    config = \
        """
        BR2_aarch64=y
        BR2_TOOLCHAIN_EXTERNAL=y
        BR2_TOOLCHAIN_EXTERNAL_LINARO_AARCH64=y
        BR2_TARGET_ARM_TRUSTED_FIRMWARE=y
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_CUSTOM_GIT=y
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_CUSTOM_REPO_URL="https://github.com/apritzel/arm-trusted-firmware.git"
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_PLATFORM="sun50iw1p1"
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_CUSTOM_REPO_VERSION="aa75c8da415158a94b82a430b2b40000778e851f"
        BR2_TARGET_ARM_TRUSTED_FIRMWARE_BL31=y
        BR2_TARGET_UBOOT=y
        BR2_TARGET_UBOOT_BUILD_SYSTEM_KCONFIG=y
        BR2_TARGET_UBOOT_CUSTOM_VERSION=y
        BR2_TARGET_UBOOT_CUSTOM_VERSION_VALUE="2020.10"
        BR2_TARGET_UBOOT_BOARD_DEFCONFIG="bananapi_m64"
        BR2_TARGET_UBOOT_NEEDS_DTC=y
        BR2_TARGET_UBOOT_NEEDS_PYTHON3=y
        BR2_TARGET_UBOOT_NEEDS_PYLIBFDT=y
        BR2_TARGET_UBOOT_NEEDS_ATF_BL31=y
        BR2_TARGET_UBOOT_FORMAT_CUSTOM=y
        BR2_TARGET_UBOOT_FORMAT_CUSTOM_NAME="u-boot.itb"
        BR2_TARGET_UBOOT_SPL=y
        BR2_TARGET_UBOOT_SPL_NAME="spl/sunxi-spl.bin"
        """

    def test_run(self):
        pass
