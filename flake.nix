{
  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config = {
            permittedInsecurePackages = [
              # "qtwebkit-5.212.0-alpha4"
              "openssl-1.1.1w"
            ];
          };
        };
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs;
            [
              # wkhtmltopdf 
              wkhtmltopdf-bin
            ];
        };
      });
}
