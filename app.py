import sys
import json
import csv

INGRESS_URL = "https://intel.ingress.com/intel?ll={}&z=17&pll={}"

def main(input_file_path,output_file_path):
    L_out = []
    L_out.append("{};{};{};{}".format('portal','url','priority','category'))
    f = open(input_file_path, 'r')
    json_data = json.load(f)
    for portals_id in json_data['portals']:
        portal_category = json_data['portals'][portals_id]['label'].rstrip()
        for portal_id in json_data['portals'][portals_id]['bkmrk']:
            try:
                portal_data = json_data['portals'][portals_id]['bkmrk'][portal_id]
                row = "{};{};{};{}".format(portal_data['label'].rstrip(),INGRESS_URL.format(portal_data['latlng'].rstrip(),portal_data['latlng'].rstrip()),str(0),portal_category)
                print(row) 
                L_out.append(row)
            except UnicodeEncodeError as e:
                print("WARNING: {}".format(e))
                continue            
    print("# portals parsed: {}".format(str(len(L_out))))
    _write_csv(output_file_path, L_out)

def _write_csv(output_file_path, L_out):
    out_file = open(output_file_path, "w")
    for line in L_out:
        # write line to output file
        out_file.write(line)
        out_file.write("\n")
    out_file.close()

if __name__ == '__main__':
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    main(input_file_path,output_file_path)