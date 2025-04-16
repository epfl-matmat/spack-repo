from spack import *
import json

from spack.version import GitVersion, StandardVersion


class Julia(Package):
    """
    The Julia Language: A fresh approach to technical computing
    This package installs the x86_64-linux-gnu version provided by Julia Computing
    """

    url  = None  # Disable default url mechanism
    homepage = "https://julialang.org/"
    list_url = "https://julialang-s3.julialang.org/bin/versions.json"
    maintainers = ["mfherbst"]

    # Julia Versions
    # fmt: off
    version("1.11.5",     sha256="723e878c642220cc0251a0e13758c059a389cadc7f01376feaf1ea7388fe8f9c")
    version("1.11.4",     sha256="fb3d3c5fccef82158a70677c0044ac5ae40410eceb0604cdc8e643eeff21df8d")
    version("1.11.3",     sha256="7d48da416c8cb45582a1285d60127ee31ef7092ded3ec594a9f2cf58431c07fd")
    version("1.11.2",     sha256="8a372ad262d4d4d55a1044f4fe3bce7c9a4a3ce8c513d2470e58e8071eecd476")
    version("1.11.1",     sha256="cca8d13dc4507e4f62a129322293313ee574f300d4df9e7db30b7b41c5f8a8f3")
    version("1.11.0-rc1", sha256="d9d7ca81087185abbb8a375c41f734deea6ea26aef2dc40d99467f8c5c7cc8d6")
    version("1.10.9",     sha256="5a2d2c5224594b683c97e7304cb72407fbcf0be4a0187789cba1a2f73f0cbf09")
    version("1.10.8",     sha256="0410175aeec3df63173c15187f2083f179d40596d36fd3a57819cc5f522ae735")
    version("1.10.7",     sha256="21b2c69806aacf191d7c81806c7d9918bddab30c7b5b8d4251389c3abe274334")
    version("1.10.4",     sha256="079f61757c3b5b40d2ade052b3cc4816f50f7ef6df668825772562b3746adff1")
    version("1.10.3",     sha256="81b910c922fff0e27ae1f256f2cc803db81f3960215281eddd2d484721928c70")
    version("1.10.2",     sha256="51bccc9bb245197f24e6b2394e6aa69c0dc1e41b4e300b796e17da34ef64db1e")
    version("1.10.1",     sha256="fe924258e55d074410b134195cf6b85cbe8f307fcd05a4fdd23f8944c5941a70")
    version("1.9.4",      sha256="07d20c4c2518833e2265ca0acee15b355463361aa4efdab858dad826cf94325c")
    version("1.8.5",      sha256="e71a24816e8fe9d5f4807664cbbb42738f5aa9fe05397d35c81d4c5d649b9d05")

    version('1.8.0', sha256='e80d732ccb7f79e000d798cb8b656dc3641ab59516d6e4e52e16765017892a00')
    version('1.7.3', sha256='9b2f4fa12d92b4dcc5d11dc66fb118c47681a76d3df8da064cc97573f2f5c739')
    version('1.7.2', sha256='a75244724f3b2de0e7249c861fbf64078257c16fb4203be78f1cf4dd5973ba95')
    version('1.7.1', sha256='44658e9c7b45e2b9b5b59239d190cca42de05c175ea86bc346c294a8fe8d9f11')
    version('1.7.0', sha256='cbf33c533d6f226161f08cdc3cec16745a3dc5afdfbaece95e3f2a5e0b6b7886')
    version('1.6.7', sha256='6c4522d595e4cbcd00157ac458a72f8aec01757053d2073f99daa39e442b2a36')
    version('1.6.6', sha256='c25ff71a4242207ab2681a0fcc5df50014e9d99f814e77cacbc5027e20514945')
    version('1.6.5', sha256='b8fe23ee547254a2fe14be587284ed77c78c06c2d8e9aad5febce0d21cab8e2c')
    version('1.6.4', sha256='52244ae47697e8073dfbc9d1251b0422f0dbd1fbe1a41da4b9f7ddf0506b2132')
    version('1.6.3', sha256='c7459c334cd7c3e4a297baf52535937c6bad640e60882f9201a73bab9394314b')
    version('1.6.2', sha256='3eb4b5775b0df1ad38f6c409e989501ab445c95bcb01ab02bd60f5bd1e823240')
    version('1.6.1', sha256='7c888adec3ea42afbfed2ce756ce1164a570d50fa7506c3f2e1e2cbc49d52506')
    version('1.6.0', sha256='463b71dc70ca7094c0e0fd6d55d130051a7901e8dec5eb44d6002c57d1bd8585')
    version('1.5.4', sha256='80dec351d1a593e8ad152636971a48d0c81bfcfab92c87f3604663616f1e8bc5')
    version('1.5.3', sha256='f190c938dd6fed97021953240523c9db448ec0a6760b574afd4e9924ab5615f1')
    version('1.5.2', sha256='6da704fadcefa39725503e4c7a9cfa1a570ba8a647c4bd8de69a118f43584630')
    version('1.5.1', sha256='f5d37cb7fe40e3a730f721da8f7be40310f133220220949939d8f892ce2e86e3')
    version('1.5.0', sha256='be7af676f8474afce098861275d28a0eb8a4ece3f83a11027e3554dcdecddb91')
    version('1.4.2', sha256='d77311be23260710e89700d0b1113eecf421d6cf31a9cebad3f6bdd606165c28')
    version('1.4.1', sha256='fd6d8cadaed678174c3caefb92207a3b0e8da9f926af6703fb4d1e4e4f50610a')
    version('1.4.0', sha256='30d126dc3598f3cd0942de21cc38493658037ccc40eb0882b3b4c418770ca751')
    version('1.3.1', sha256='faa707c8343780a6fe5eaf13490355e8190acf8e2c189b9e7ecbddb0fa2643ad')
    version('1.3.0', sha256='9ec9e8076f65bef9ba1fb3c58037743c5abb3b53d845b827e44a37e7bcacffe8')
    version('1.2.0', sha256='926ced5dec5d726ed0d2919e849ff084a320882fb67ab048385849f9483afc47')
    version('1.1.1', sha256='f0a83a139a89a2ccf2316814e5ee1c0c809fca02cbaf4baf3c1fd8eb71594f06')
    version('1.1.0', sha256='80cfd013e526b5145ec3254920afd89bb459f1db7a2a3f21849125af20c05471')
    version('1.0.5', sha256='9dedd613777ba6ebd8aee5796915ff50aa6188ea03ed143cb687fc2aefd76b03')
    version('1.0.4', sha256='bb9e33d95f47e703d9199f0358c038c61259e2ff9f3fd515c919729ace89443c')
    version('1.0.3', sha256='362ba867d2df5d4a64f824e103f19cffc3b61cf9d5a9066c657f1c5b73c87117')
    version('1.0.2', sha256='e0e93949753cc4ac46d5f27d7ae213488b3fef5f8e766794df0058e1b3d2f142')
    version('1.0.1', sha256='9ffbcf7f4a111e13415954caccdd1ce90b5c835cee9f62d6ac708f5b752c87dd')
    version('1.0.0', sha256='bea4570d7358016d8ed29d2c15787dbefaea3e746c570763e7ad6040f17831f3')
    # fmt: on

    # Sanity Checks
    sanity_check_is_file = [join_path("bin", "julia")]
    sanity_check_is_dir = ["bin", "etc", "include", "lib", "libexec", "share"]

    def url_for_version(self, version):
        """Generate download url for a specific version of Julia"""
        url = "https://julialang-s3.julialang.org/bin/linux/x64/{0}/julia-{1}-linux-x86_64.tar.gz"
        return url.format(version.up_to(2), version)

    def fetch_remote_versions(self, concurrency=128):
        # Fetch versions from JuliaLang
        _, _, resp = spack.util.web.read_from_url(self.list_url)
        all_versions = json.load(resp)
        versions = dict()
        for k, v in all_versions.items():
            for files in v["files"]:
                if files["triplet"].strip() == "x86_64-linux-gnu":
                    versions[k] = files["url"]

        return versions

    def install(self, spec, prefix):
        install_tree(".", prefix)

    @run_after("install")
    def check_version(self):
        # Check that installed version matches the requested version
        self.run_test(
            join_path(self.prefix, "bin", "julia"),
            options=["--version"],
            expected=[f"julia version {self.version}"],
        )

    def test(self):
        """Run Julia's Test Suite"""
        self.run_test(
            join_path(self.prefix, "bin", "julia"),
            options=["--eval", "Base.runtests(; exit_on_error=true)"],
            installed=True,
        )
