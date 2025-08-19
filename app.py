
import argparse, json
from pathlib import Path
import pandas as pd
from utils import extract_text, detect, severity

def scan_folder(input_dir: Path):
    rows = []
    for p in sorted(Path(input_dir).glob("**/*")):
        if p.is_dir():
            continue
        text = extract_text(p)
        f = detect(text)
        sev = severity(f)
        rows.append({
            "file": str(p),
            "severity": sev,
            "aadhaar_hits": len(f["aadhaar"]),
            "pan_hits": len(f["pan"]),
            "email_count": len(f["emails"]),
            "password_phrase": f["password_phrase"],
            "emails_sample": ", ".join(f["emails"][:3])
        })
    return pd.DataFrame(rows)

def save_reports(df: pd.DataFrame, outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)
    df.to_csv(outdir / "results.csv", index=False)
    df.to_json(outdir / "results.json", orient="records", indent=2)

def charts(df: pd.DataFrame, outdir: Path):
    import matplotlib.pyplot as plt
    # Severity bar chart
    counts = df["severity"].value_counts().reindex(["Critical","Medium","Low","None"]).fillna(0)
    plt.figure()
    counts.plot(kind="bar")
    plt.title("Findings by Severity")
    plt.xlabel("Severity")
    plt.ylabel("File Count")
    plt.tight_layout()
    plt.savefig(outdir / "severity_chart.png")
    plt.close()

    # Results table as image
    # Show key columns only
    cols = ["file","severity","aadhaar_hits","pan_hits","email_count","password_phrase"]
    fig, ax = plt.subplots()
    ax.axis("off")
    table = ax.table(cellText=df[cols].values, colLabels=cols, loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.4)
    plt.tight_layout()
    plt.savefig(outdir / "results_table.png", dpi=200, bbox_inches="tight")
    plt.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Input folder with files to scan")
    ap.add_argument("--outdir", required=True, help="Output folder for reports & images")
    args = ap.parse_args()

    df = scan_folder(Path(args.input))
    save_reports(df, Path(args.outdir))
    charts(df, Path(args.outdir))

    print("Scan complete. Reports saved to:", args.outdir)

if __name__ == "__main__":
    main()
