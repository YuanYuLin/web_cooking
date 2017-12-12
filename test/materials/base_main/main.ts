<%
import cook_template

ng4_imports = root_obj["NG4_IMPORTS"]
%>
{{cook_template.generate_import_header(root_obj)}}

if (environment.production) {
  enableProdMode();
}

platformBrowserDynamic().bootstrapModule(AppModule);

