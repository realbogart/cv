{
  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          # config = {
          #   permittedInsecurePackages = [
          #     # When building wkhtmltopdf from source
          #     "qtwebkit-5.212.0-alpha4"
          #
          #     # wkhtmltopdf-bin
          #     "openssl-1.1.1w"
          #   ];
          # };
        };
        dependencies = with pkgs; [
          # wkhtmltopdf 
          # wkhtmltopdf-bin
          puppeteer-cli
          # open-sans
          # arkpandora_ttf
          python3
          # htmldoc
          xdg-utils
        ];
      in {
        devShells.default = pkgs.mkShell { buildInputs = dependencies; };
        packages.default = pkgs.stdenv.mkDerivation {
          name = "cv";
          inherit system;
          src = ./.;
          buildInputs = dependencies;
          dontUnpack = true;
          preConfigure = ''
            export FONT_PATH=$src
          '';
          installPhase = ''
            cd $src
            echo "FONT_PATH set to $FONT_PATH"
            echo "Building CV..."
            mkdir $out
            sleep 1
            puppeteer print --margin-top 0 --margin-right 0 --margin-bottom 0 --margin-left 0 index.html $out/cv.pdf
          '';
        };
        apps.default = {
          type = "app";
          program = "${pkgs.xdg-utils}/bin/xdg-open ${
              self.packages.${system}.default
            }/cv.pdf";
        };
      });
}
